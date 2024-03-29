from mreza import Mreza
from Vozilo import Vozilo
from prepreka import Semafor, Prelaz
import random

class Simulacija():
    def __init__(self):
        self.mreza = Mreza()
        self.vozila = []

    def setup(self):
        # Garaza i raskrsnice
        self.mreza.dodajGarazu(1, 5, (0, 0), [2, 5, 4])
        self.mreza.dodajRaskrsnicu(2, (0, 0), [1, 5, 3], [5, 3])
        self.mreza.dodajRaskrsnicu(3, (0, 0), [2, 4, 5], [2, 4, 5])
        self.mreza.dodajRaskrsnicu(4, (0, 0), [1, 5, 3], [5, 3])
        self.mreza.dodajRaskrsnicu(5, (0, 0), [1, 2, 3, 4], [2, 3, 4])

        # Putevi
        self.mreza.dodajPut(1, 10, 60, (1, 2), Semafor(False))
        self.mreza.dodajPut(2, 10, 60, (1, 5))
        self.mreza.dodajPut(3, 10, 60, (1, 4))
        self.mreza.dodajPut(4, 10, 60, (4, 5), Semafor(False))
        self.mreza.dodajPut(5, 10, 60, (5, 4))
        self.mreza.dodajPut(6, 10, 60, (5, 2))
        self.mreza.dodajPut(7, 10, 60, (2, 5), Semafor(False))
        self.mreza.dodajPut(8, 10, 60, (5, 3), Semafor(False))
        self.mreza.dodajPut(9, 10, 60, (3, 5))
        self.mreza.dodajPut(10, 10, 60, (2, 3))
        self.mreza.dodajPut(11, 10, 60, (3, 2))
        self.mreza.dodajPut(12, 10, 60, (3, 4), Semafor(False))
        self.mreza.dodajPut(13, 10, 60, (4, 3))
    
    def dodaj_vozilo(self, vozilo):
        self.vozila.append(vozilo)

    def start(self):
        # Doesn't support threading for now
        for vozilo in self.vozila:
            vozilo.Vozi(self.mreza)

if __name__ == "__main__":
    sim = Simulacija()
    sim.setup()
    sim.dodaj_vozilo(Vozilo("auto", 1))
    sim.start()