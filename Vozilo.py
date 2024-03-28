class Vozilo:

    def __init__(self, tip : str, id : str) -> None:
        self._tip = tip
        self._id = id
        self._duzina = None
        self._brzina = None
        if tip == 'auto':
            self._brzina = 5
            self._duzina = 2
        else:
            raise Exception("Nedefinisan tip vozila!")
    
    def Uzmi_duzinu(self) -> int:
        return self._duzina
    
    def Uzmi_id(self) -> str:
        return self._id
    
    def Uzmi_brzinu(self) -> int:
        return self._brzina
    
    def Uzmi_tip(self) -> str:
        return self._tip