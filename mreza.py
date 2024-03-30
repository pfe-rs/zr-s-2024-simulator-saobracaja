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
