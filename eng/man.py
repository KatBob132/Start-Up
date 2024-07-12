from pygame.locals import *
import pygame as pg

from time import time as tme
from sys import exit as ext

scn = {}

scn["siz"] = (328, 256)
scn["pix-siz"] = 3

scn["srf"] = pg.Surface(scn["siz"])

scn["win"] = None
scn["win-bck"] = None

siz = (scn["siz"][0] * scn["pix-siz"], scn["siz"][1] * scn["pix-siz"])

tme_cal = {}
fps_cal = {}

tme_cal["str"] = tme()
tme_cal["now"] = 0
tme_cal["dlt"] = 0

fps_cal["fps"] = 0
fps_cal["fps-lit"] = []
fps_cal["fps-avg"] = 0

pg.init()
dpy = pg.display.set_mode(siz, DOUBLEBUF)
pg.display.set_caption("Verlet Inter")
fps = pg.time.Clock()

while True:
    dpy.fill("white")
    scn["srf"].fill("white")

    tme_cal["now"] = tme()
    tme_cal["dlt"] = (tme_cal["now"] - tme_cal["str"])
    tme_cal["str"] = tme()

    fps_cal["fps"] = 1 / tme_cal["dlt"]
    fps_cal["fps-lit"].append(fps_cal["fps"])

    while len(fps_cal["fps-lit"]) > round(fps_cal["fps"]):
        fps_cal["fps-lit"].pop(0)
    
    fps_cal["fps-avg"] = round(sum(fps_cal["fps-lit"]) / len(fps_cal["fps-lit"]))

    for evt in pg.event.get():
        if evt.type == pg.QUIT:
            pg.quit()
            ext()

        if evt.type == pg.KEYDOWN:
            if evt.key == pg.K_ESCAPE:
                pg.quit()
                ext()

    scn["win"] = pg.transform.scale(scn["srf"], siz)
    scn["win-bck"] = pg.transform.scale(scn["srf"], siz)

    scn["win-bck"].set_alpha(51)

    dpy.blit(scn["win"], (0, 0))
    dpy.blit(scn["win-bck"], (scn["pix-siz"], scn["pix-siz"]))

    pg.display.update()
    pg.display.flip()
    fps.tick(0)