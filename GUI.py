import pygame as pg
import random
from mreza import *
from Put import Put

@staticmethod
def Nacrtaj_raskrsnicu(raskrsnica : Raskrsnica, ekran, boja : tuple[int, int, int], r : int):
    pg.draw.circle(ekran, boja, raskrsnica.Uzmi_koordinate(), r)

@staticmethod
def Nacrtaj_put(put : Put, ekran, boja : tuple[int, int, int], r : int, raskrsnice : list[Raskrsnica]):
    x1, y1 = Trazena_raskrsnica(raskrsnice, put.Uzmi_raskrsnice()[0]).Uzmi_koordinate()
    x2, y2 = Trazena_raskrsnica(raskrsnice, put.Uzmi_raskrsnice()[1]).Uzmi_koordinate()

    pg.draw.line(ekran, boja, (x1, y1), (x2, y2), r)

@staticmethod
def Trazena_raskrsnica(raskrsnice : list [Raskrsnica], id : int) -> Raskrsnica:
    for raskrsnica in raskrsnice:
        if id == raskrsnica.Uzmi_id():
            return raskrsnica

@staticmethod
def Pronadjen(lista : list[tuple[int, int]], tuple : tuple[int, int]):
    for clan in lista:
        if clan == tuple: return True
    return False

pg.init()


sirina, visina = 1500, 1000
ekran = pg.display.set_mode((sirina, visina))
pg.display.set_caption("Simulacija saobracaja")

zelena = (0, 255, 0)
crna = (0, 0, 0)
bela = (255, 255, 255)

mreza = Mreza()

# Garaza i raskrsnice
mreza.dodajGarazu(1, 5, (100, 50), [2, 5, 4])
mreza.dodajRaskrsnicu(2, (1400, 50), [1, 5, 3], [5, 3])
mreza.dodajRaskrsnicu(3, (1400, 950), [2, 4, 5], [2, 4, 5])
mreza.dodajRaskrsnicu(4, (100, 950), [1, 5, 3], [5, 3])
mreza.dodajRaskrsnicu(5, (750, 500), [1, 2, 3, 4], [2, 3, 4])

# Putevi
mreza.dodajPut(1, 1300, 5, (1, 2), Semafor(False))
mreza.dodajPut(2, int((650 ** 2 + 450 ** 2) ** .5), 5, (1, 5))
mreza.dodajPut(3, 900, 5, (1, 4))
mreza.dodajPut(4, int((650 ** 2 + 450 ** 2) ** .5), 5, (4, 5), Semafor(False))
mreza.dodajPut(5, int((650 ** 2 + 450 ** 2) ** .5), 5, (5, 4))
mreza.dodajPut(6, int((650 ** 2 + 450 ** 2) ** .5), 5, (5, 2))
mreza.dodajPut(7, int((650 ** 2 + 450 ** 2) ** .5), 5, (2, 5), Semafor(False))
mreza.dodajPut(8, int((650 ** 2 + 450 ** 2) ** .5), 5, (5, 3), Semafor(False))
mreza.dodajPut(9, int((650 ** 2 + 450 ** 2) ** .5), 5, (3, 5))
mreza.dodajPut(10, 900, 5, (2, 3))
mreza.dodajPut(11, 900, 5, (3, 2))
mreza.dodajPut(12, 1300, 5, (3, 4), Semafor(False))
mreza.dodajPut(13, 1300, 5, (4, 3))

radi = True
while radi:
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            radi = False

    ekran.fill(zelena)

    for raskrsnica in mreza.raskrsnice:
        Nacrtaj_raskrsnicu(raskrsnica, ekran, crna, 9)
    
    iscrtani_putevi = []
    for put in mreza.putevi:
        pocetak, kraj = put.Uzmi_raskrsnice()
        iscrtani_putevi.append((pocetak, kraj))
        if Pronadjen(iscrtani_putevi, (kraj, pocetak)): r = 10
        else: r = 5

        Nacrtaj_put(put, ekran, crna, r, mreza.raskrsnice)

    pg.display.flip()

pg.quit()