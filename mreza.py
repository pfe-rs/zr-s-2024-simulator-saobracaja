from Put import Put
from Raskrsnica import Raskrsnica, Garaza
from Vozilo import Vozilo
from prepreka import Semafor, Prelaz
import random

class Mreza: 
    def __init__(self):
        self.garaze = []
        self.raskrsnice = []
        self.putevi = []
    
    def dodajRaskrsnicu(self, id, koordinate, ulazni_putevi, izlazni_putevi):
        raskrsnica = Raskrsnica(id, koordinate)
        raskrsnica._ulazni_putevi = ulazni_putevi
        raskrsnica._izlazni_putevi = izlazni_putevi
        self.raskrsnice.append(raskrsnica)

    def dodajGarazu(self, id, vreme_stvaranja, koordinate, izlazni_putevi):
        self.dodajRaskrsnicu(id, koordinate, [id for _ in range(len(izlazni_putevi))], izlazni_putevi)
        self.garaze.append(Garaza(id, koordinate, vreme_stvaranja, id))
    
    def dodajPut(self, id, duzina, max_brzina, id_raskrsnica, prepreka=None):
        self.putevi.append(Put(duzina, max_brzina, id, id_raskrsnica, prepreka))

    def start(self, vehicles):
        # Doesn't support threading for now
        for vehicle in vehicles:
            queue = []
            queue.append(mreza.raskrsnice[0])
            while len(queue) != 0:
                front = queue[len(queue) - 1]
                #print(f"{front._id}")
                queue.pop()
                nextNode = random.choice(front._izlazni_putevi)
                endConns = (front._id, nextNode)
                for put in mreza.putevi:
                    if put._id_raskrsnica == endConns:
                        currentRoad = put

                for put in mreza.putevi:
                    if put._id_raskrsnica == endConns:
                        putID, voziloID = put._id, vehicle.Uzmi_id()
                        yield (putID, voziloID)

                if currentRoad._semafor == None:
                    for raskrsnica in mreza.raskrsnice:
                        if raskrsnica._id == nextNode:
                            queue.append(raskrsnica)
                else:
                    # Doesn't support threading for now
                    if not currentRoad._semafor.stanje:
                        currentRoad.Azuriraj_semafor()
                    print("Zeleno")
                    
                    for raskrsnica in mreza.raskrsnice:
                        if raskrsnica._id == nextNode:
                            queue.append(raskrsnica)


if __name__ == "__main__":
    mreza = Mreza()
    
    # Garaza i raskrsnice
    mreza.dodajGarazu(1, 5, (0, 0), [2, 5, 4])
    mreza.dodajRaskrsnicu(2, (0, 0), [1, 5, 3], [5, 3])
    mreza.dodajRaskrsnicu(3, (0, 0), [2, 4, 5], [2, 4, 5])
    mreza.dodajRaskrsnicu(4, (0, 0), [1, 5, 3], [5, 3])
    mreza.dodajRaskrsnicu(5, (0, 0), [1, 2, 3, 4], [2, 3, 4])

    # Putevi
    mreza.dodajPut(1, 10, 60, (1, 2), Semafor(False))
    mreza.dodajPut(2, 10, 60, (1, 5))
    mreza.dodajPut(3, 10, 60, (1, 4))
    mreza.dodajPut(4, 10, 60, (4, 5), Semafor(False))
    mreza.dodajPut(5, 10, 60, (5, 4))
    mreza.dodajPut(6, 10, 60, (5, 2))
    mreza.dodajPut(7, 10, 60, (2, 5), Semafor(False))
    mreza.dodajPut(8, 10, 60, (5, 3), Semafor(False))
    mreza.dodajPut(9, 10, 60, (3, 5))
    mreza.dodajPut(10, 10, 60, (2, 3))
    mreza.dodajPut(11, 10, 60, (3, 2))
    mreza.dodajPut(12, 10, 60, (3, 4), Semafor(False))
    mreza.dodajPut(13, 10, 60, (4, 3))
    
    putanja = mreza.start([Vozilo("auto", 1)])
    while True:
        print(next(putanja))

    #for put in mreza.putevi:
    #    print(f"{put._id}. put povezuje {put._id_raskrsnica[0]}. raskrsnicu i {put._id_raskrsnica[1]}. raskrsnicu")