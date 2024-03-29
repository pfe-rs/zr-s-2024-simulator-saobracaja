from Vozilo import Vozilo

class Put:
    
    def __init__(self, duzina : int, max_brzina : int, id : int, id_raskrsnica : tuple[int, int], semafor = None) -> None:
        self._duzina = duzina
        self._max_brzina = max_brzina
        self._id = id
        self._id_raskrsnica = id_raskrsnica
        self._semafor = semafor
        self.prostor_na_ulici = [None for _ in range(duzina)]
        self._slobodno_mesto = duzina

    def Uzmi_duzinu(self) -> int:
        return self._duzina
    
    def Uzmi_id(self) -> int:
        return self._id

    def Uzmi_max_brzinu(self) -> int:
        return self._max_brzina

    def Uzmi_raskrsnice(self) -> tuple[int, int]:
        return self._id_raskrsnica

    def Proveri_semafor(self):
        return self._semafor.stanje
    
    def Azuriraj_semafor(self) -> None:
        self._semafor = self._semafor.Promeni_stanje()
    
    def Ima_mesta(self) -> int:
        return self._slobodno_mesto
    
    def Dodaj_vozilo(self, vozilo : Vozilo) -> None:    # Mora da se pozove iskljucivo nakon provere da li ima prostora na ulici za dato vozilo !!
        self.prostor_na_ulici[:vozilo.Uzmi_duzinu()] = vozilo