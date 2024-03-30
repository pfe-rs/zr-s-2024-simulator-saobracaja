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
        self.mreza.dodajGarazu(1, 5, (100, 50), [2, 5, 4])
        self.mreza.dodajRaskrsnicu(2, (1400, 50), [1, 5, 3], [5, 3])
        self.mreza.dodajRaskrsnicu(3, (1400, 950), [2, 4, 5], [2, 4, 5])
        self.mreza.dodajRaskrsnicu(4, (100, 950), [1, 5, 3], [5, 3])
        self.mreza.dodajRaskrsnicu(5, (750, 500), [1, 2, 3, 4], [2, 3, 4])

        # Putevi
        self.mreza.dodajPut(1, 1300, 5, (1, 2), Semafor(False))
        self.mreza.dodajPut(2, int((650 ** 2 + 450 ** 2) ** .5), 5, (1, 5))
        self.mreza.dodajPut(3, 900, 5, (1, 4))
        self.mreza.dodajPut(4, int((650 ** 2 + 450 ** 2) ** .5), 5, (4, 5), Semafor(False))
        self.mreza.dodajPut(5, int((650 ** 2 + 450 ** 2) ** .5), 5, (5, 4))
        self.mreza.dodajPut(6, int((650 ** 2 + 450 ** 2) ** .5), 5, (5, 2))
        self.mreza.dodajPut(7, int((650 ** 2 + 450 ** 2) ** .5), 5, (2, 5), Semafor(False))
        self.mreza.dodajPut(8, int((650 ** 2 + 450 ** 2) ** .5), 5, (5, 3), Semafor(False))
        self.mreza.dodajPut(9, int((650 ** 2 + 450 ** 2) ** .5), 5, (3, 5))
        self.mreza.dodajPut(10, 900, 5, (2, 3))
        self.mreza.dodajPut(11, 900, 5, (3, 2))
        self.mreza.dodajPut(12, 1300, 5, (3, 4), Semafor(False))
        self.mreza.dodajPut(13, 1300, 5, (4, 3))
    
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