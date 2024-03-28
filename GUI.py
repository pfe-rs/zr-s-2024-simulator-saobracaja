import pygame as pg
import random
from Raskrsnica import Raskrsnica

@staticmethod
def Nacrtaj_raskrsnicu(raskrsnica : Raskrsnica, ekran, boja : tuple[int, int, int], r : int):
    pg.draw.circle(ekran, boja, raskrsnica.Uzmi_koordinate(), r)


pg.init()


sirina, visina = 1500, 1000
ekran = pg.display.set_mode((sirina, visina))
pg.display.set_caption("Simulacija saobracaja")

zelena = (0, 255, 0)
crna = (0, 0, 0)
bela = (255, 255, 255)

broj_raskrsnica = 10
raskrsnice = Raskrsnica.Generisi_raskrsnice(broj_raskrsnica, (sirina, visina))

radi = True
while radi:
    for dogadjaj in pg.event.get():
        if dogadjaj.type == pg.QUIT:
            radi = False

    ekran.fill(zelena)

    for raskrsnica in raskrsnice:
        Nacrtaj_raskrsnicu(raskrsnica, ekran, crna, 4)

    pg.display.flip()

pg.quit()