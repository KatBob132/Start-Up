from scripts.functions import *
from scripts.objects import *
from scripts.utils import *

from pygame.locals import *
import pygame as pg

from time import time
from sys import exit

color = import_data("engine/data/color.json").get_data()
screen = {}

screen["size"] = (328, 256)
screen["pixel-size"] = 3

screen["surface"] = pg.Surface(screen["size"])

screen["window"] = None
screen["window-back"] = None

size = (screen["size"][0] * screen["pixel-size"], screen["size"][1] * screen["pixel-size"])
tick = 0
text = text_master("engine/data/font.json", screen["surface"])

time_cal = {}
delta = {}

time_cal["elapsed-time"] = 1
time_cal["past-time"] = time()

time_cal["frame-count"] = 0
time_cal["fps"] = 0

delta["delta"] = 0
delta["past-time"] = time()

pg.init()
flags = DOUBLEBUF
display = pg.display.set_mode(size, flags)
pg.display.set_caption("Game")
fps = pg.time.Clock()

mouse_data = {"xy": [pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]]}
mouse_data["world-xy"] = [int(mouse_data["xy"][0] / screen["pixel-size"]), int(mouse_data["xy"][1] / screen["pixel-size"])]
mouse_data["buttons"] = [False, False, False]

while True:
    display.fill(color["white"])
    screen["surface"].fill(color["white"])

    pg.mouse.set_visible(False)

    mouse_data["xy"] = [pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]]
    mouse_data["world-xy"] = [int(mouse_data["xy"][0] / screen["pixel-size"]), int(mouse_data["xy"][1] / screen["pixel-size"])]

    time_cal["frame-count"] += 1
    time_cal["elapsed-time"] = time() - time_cal["past-time"]

    if time_cal["elapsed-time"] > 1:
        time_cal["fps"] = round(time_cal["frame-count"] / time_cal["elapsed-time"])
        time_cal["frame-count"] = 0
        time_cal["past-time"] = time()

    delta["delta"] = (pg.time.get_ticks() - delta["past-time"]) / 1000
    delta["past-time"] = pg.time.get_ticks()
    
    text.draw_text(time_cal["fps"], (1, 1), 1, color["red"], 1)

    pg.draw.rect(screen["surface"], color["red"], pg.Rect(mouse_data["world-xy"][0], mouse_data["world-xy"][1], 1, 1))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()

    screen["window"] = pg.transform.scale(screen["surface"], size)
    screen["window-back"] = pg.transform.scale(screen["surface"], size)

    screen["window-back"].set_alpha(51)

    display.blit(screen["window"], (0, 0))
    display.blit(screen["window-back"], (screen["pixel-size"], screen["pixel-size"]))

    pg.display.update()
    pg.display.flip()
    fps.tick(tick)