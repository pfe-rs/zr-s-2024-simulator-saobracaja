import pygame as pg
import random
from Simulacija import *
from Raskrsnica import Raskrsnica
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

sim = Simulacija()
sim.setup()
for i in range(3):
    sim.dodaj_vozilo(Vozilo('auto', i + 1))


radi = True
while radi:
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            radi = False

    ekran.fill(zelena)

    for raskrsnica in sim.mreza.raskrsnice:
        Nacrtaj_raskrsnicu(raskrsnica, ekran, crna, 5)
    
    iscrtani_putevi = []
    for put in sim.mreza.putevi:
        pocetak, kraj = put.Uzmi_raskrsnice()
        iscrtani_putevi.append((pocetak, kraj))
        if Pronadjen(iscrtani_putevi, (kraj, pocetak)): r = 20
        else: r = 10

        Nacrtaj_put(put, ekran, crna, r, sim.mreza.raskrsnice)

    

    pg.display.flip()

pg.quit()