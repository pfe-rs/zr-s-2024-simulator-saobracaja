from Put import Put

class Vozilo:

    def __init__(self, tip : str, id : str) -> None:
        self._tip = tip
        self._id = id
        self._duzina = None
        self._brzina = None
        self._mesto_na_putu = 0
        if tip == 'auto':
            self._brzina = 5
            self._duzina = 2
        else:
            raise Exception("Nedefinisan tip vozila!")
    
    def Pomeri_vozilo(self, put : Put):
        put.Azuriraj_semafor()
        brzina = min(put.Uzmi_max_brzinu(), self.Uzmi_brzinu())
        mesto = self.Uzmi_mesto_na_putu()
        promena_mesta = 0
        if put.Proveri_semafor():
            if mesto + brzina >= put.Uzmi_duzinu():
                pass # ovde mora da prodje kroz raskrsnicu
            else:
                for i in range(brzina):
                    if put.prostor_na_ulici[mesto + i] == None:
                        promena_mesta += 1
                    else: break
                for i in range(self.Uzmi_duzinu()):
                    put.prostor_na_ulici[mesto + i + promena_mesta] = put.prostor_na_ulici[mesto + i]
                    put.prostor_na_ulici[mesto + i] = None


    
    def Uzmi_mesto_na_putu(self) -> int:
        return self._mesto_na_putu
    
    def Uzmi_duzinu(self) -> int:
        return self._duzina
    
    def Uzmi_id(self) -> str:
        return self._id
    
    def Uzmi_brzinu(self) -> int:
        return self._brzina
    
    def Uzmi_tip(self) -> str:
        return self._tip