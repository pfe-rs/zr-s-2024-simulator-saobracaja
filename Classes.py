
class Vozilo:

    def __init__(self, tip : str, id : int) -> None:
        self._tip = tip
        self._id = id
        self._duzina = None
        self._brzina = None
        if tip == 'auto':
            self._brzina = 5
            self._duzina = 2
        else:
            raise Exception("Nedefinisan tip vozila!")
    
    def Uzmi_duzinu(self):
        return self._duzina
    
    def Uzmi_id(self):
        return self._id
    
    def Uzmi_brzinu(self):
        return self._brzina
    
    def Uzmi_tip(self):
        return self._tip
    
class Put:
    
    def __init__(self, duzina : int, max_brzina : int, id : int, id_raskrsnica : tuple[int, int], semafor) -> None:
        self._duzina = duzina
        self._max_brzina = max_brzina
        self._id = id
        self._id_raskrsnica = id_raskrsnica
        self._semafor = semafor
        self.prostor_na_ulici = [None for _ in range(duzina)]
        self._slobodno_mesto = duzina
    
    def Uzmi_id(self) -> int:
        return self._id

    def Uzmi_max_brzinu(self) -> int:
        return self._max_brzina

    def Uzmi_raskrsnice(self) -> tuple[int, int]:
        return self._id_raskrsnica

    def Proveri_semafor(self):
        return self._semafor._stanje
    
    def Azuriraj_semafor(self) -> None:
        self._semafor = self._semafor.Promeni_stanje()
    
    def Ima_mesta(self) -> int:
        return self._slobodno_mesto

    def Pomeri_vozila(self) -> Vozilo:
        self.Azuriraj_semafor()
        if self.Proveri_semafor():
            vozilo = self.prostor_na_ulici[-1]
            self.prostor_na_ulici = [None] + self.prostor_na_ulici[:-1]
            return vozilo
        else:
            for i in range(self._duzina - 1, 0, -1):
                if self.prostor_na_ulici[i] == None:
                    self.prostor_na_ulici[:i] = [None] + self.prostor_na_ulici[:i - 1]
                    return
    
    def Dodaj_vozilo(self, vozilo : Vozilo) -> None:    # Mora da se pozove iskljucivo nakon provere da li ima prostora na ulici za dato vozilo !!
        self.prostor_na_ulici[:vozilo.Uzmi_duzinu()] = vozilo

