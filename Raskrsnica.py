import random
from Vozilo import Vozilo

class Raskrsnica:

    def __init__(self, id : int, koordinate : tuple[int, int]) -> None:
        self._id = id
        self._ulazni_putevi = []
        self._izlazni_putevi = []
        self._koordinate = koordinate

    def Uzmi_koordinate(self) -> tuple[int, int]:
        return self._koordinate

    def Uzmi_id(self) -> int:
        return self._id


class Garaza(Raskrsnica):

    dostupni_tipovi_vozila = ['auto']

    def __init__(self, id: int, koordinate: tuple[int, int], vreme_stvaranja : float, id_raskrsnice : int) -> None:
        super().__init__(id, koordinate)
        self._vreme_stvaranja = vreme_stvaranja
        self._izlazni_putevi = [id_raskrsnice]
        self._napravljenih_vozila = 1
    
    def Uzmi_id(self) -> int:
        return self._id

    def Uzmi_broj_vozila(self) -> int:
        return self._napravljenih_vozila
    
    def Uvecaj_broj_vozila(self) -> None:
        self._napravljenih_vozila += 1
    
    def Stvori_vozilo(self):
        tip = random.choice(Garaza.dostupni_tipovi_vozila)
        id = str(self.Uzmi_id()) + "_" + str(self.Uzmi_broj_vozila())
        self.Uvecaj_broj_vozila()
        vozilo = Vozilo(tip, id)
        return vozilo