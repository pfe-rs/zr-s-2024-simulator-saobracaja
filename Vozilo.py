import random

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
    
    def Pomeri_vozilo(self, put, sledeca_raskrsnica_id, putevi):
        put.Azuriraj_semafor()
        brzina = min(put.Uzmi_max_brzinu(), self.Uzmi_brzinu())
        mesto = self.Uzmi_mesto_na_putu()
        promena_mesta = 0
        if put.Proveri_semafor():
            if mesto + brzina >= put.Uzmi_duzinu():
                sledeci_put_id_raskrsnica = (put.Uzmi_raskrsnice()[1], sledeca_raskrsnica_id)
                for put in putevi:
                    if put.Uzmi_raskrsnice() == sledeci_put_id_raskrsnica:
                        trazeni_put = put
                
                trazeni_put.Dodaj_vozilo(self)
                self._mesto_na_putu[mesto:] = None

            else:
                for i in range(brzina):
                    if put.prostor_na_ulici[mesto + i] == None:
                        promena_mesta += 1
                    else: break
                for i in range(self.Uzmi_duzinu()):
                    put.prostor_na_ulici[mesto + i + promena_mesta] = put.prostor_na_ulici[mesto + i]
                    put.prostor_na_ulici[mesto + i] = None
    
    def Vozi(self, mreza):
            queue = []
            queue.append(mreza.raskrsnice[0])
            while len(queue) != 0:
                tren_raskrsnica = queue[len(queue) - 1]
                queue.pop()
                sledeca_raskrsnica_id = random.choice(tren_raskrsnica._izlazni_putevi)
                trazeni_put = (tren_raskrsnica._id, sledeca_raskrsnica_id)
                for put in mreza.putevi:
                    if put.Uzmi_id() == trazeni_put:
                        trenutni_put = put

                self.Pomeri_vozilo(trenutni_put, sledeca_raskrsnica_id, mreza.putevi)

                if trenutni_put._semafor == None:
                    for raskrsnica in mreza.raskrsnice:
                        if raskrsnica._id == sledeca_raskrsnica_id:
                            queue.append(raskrsnica)
                else:
                    # Doesn't support threading for now
                    if not trenutni_put._semafor.stanje:
                        trenutni_put.Azuriraj_semafor()
                    
                    for raskrsnica in mreza.raskrsnice:
                        if raskrsnica._id == sledeca_raskrsnica_id:
                            queue.append(raskrsnica)


    
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