
class Put:
    
    def __init__(self, duzina : int, max_brzina : int, id : int, id_raskrsnica : tuple[int, int], semafor : Prepreka) -> None:
        self._duzina = duzina
        self._max_brzina = max_brzina
        self._id = id
        self._id_raskrsnica = id_raskrsnica
        self._semafor = semafor
        self.prostor_na_ulici = [None for _ in range(duzina)]
        self._slobodno_mesto = duzina
    
    def UzmiId(self):
        return self._id

    def UzmiMaxBrzinu(self):
        return self._max_brzina

    def UzmiRaskrsnice(self):
        return self._id_raskrsnica

    def ProveriSemafor(self):
        return self._semafor._stanje
    
    def AzurirajSemafor(self):
        self._semafor = self._semafor.Azuriraj()
    
    def ImaMesta(self):
        return self._slobodno_mesto

    def PomeriVozila(self):
        self.AzurirajSemafor()
        if self.ProveriSemafor():
            vozilo = self.prostor_na_ulici[-1]
            self.prostor_na_ulici = [None] + self.prostor_na_ulici[:-1]
            return vozilo
        else:
            for i in range(self._duzina - 1, 0, -1):
                if self.prostor_na_ulici[i] == None:
                    self.prostor_na_ulici[:i] = [None] + self.prostor_na_ulici[:i - 1]
                    return
    
    def DodajVozilo(self, vozilo : Vozilo): # Mora da se pozove iskljucivo nakon provere da li ima prostora na ulici za dato vozilo !!
        self.prostor_na_ulici[:vozilo.UzmiDuzinu()] = vozilo


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
    
    def UzmiDuzinu(self):
        return self._duzina
    
    def UzmiId(self):
        return self._id
    
    def UzmiBrzinu(self):
        return self._brzina
    
    def UzmiTip(self):
        return self._tip