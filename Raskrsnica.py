import random


class Raskrsnica:

    def __init__(self, id : int, koordinate : tuple[int, int]) -> None:
        self._id = id
        self._ulazni_putevi = []
        self._izlazni_putevi = []
        self._koordinate = koordinate

    def Uzmi_koordinate(self) -> tuple[int, int]:
        return self._koordinate
    
    @staticmethod
    def Generisi_raskrsnice(broj_raskrsnica : int, dimenzije_ekrana : tuple[int, int]) -> list[Raskrsnica]:
        raskrsnice = []
        sirina, visina = dimenzije_ekrana
        for i in range(broj_raskrsnica):
            x = random.randint(10, sirina - 10)
            y = random.randint(10, visina - 10)
            raskrsnica = Raskrsnica(i, (x, y))
            raskrsnice.append(raskrsnica)
        
        return raskrsnice


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
        id = self.Uzmi_id() + "_" + self.Uzmi_broj_vozila()
        self.Uvecaj_broj_vozila()
        vozilo = Vozilo(tip, id)
        return vozilo