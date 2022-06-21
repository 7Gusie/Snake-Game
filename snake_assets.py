import pygame as pg

pg.init()
pg.font.init()

window = pg.display.set_mode([1000, 700])
pg.display.set_caption("Snake Game")

font = pg.font.SysFont("Lucida Console", 30)

color_indigo = (75, 0, 130)

score = 0