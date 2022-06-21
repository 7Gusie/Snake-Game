import pygame as pg

pg.init()
pg.font.init()

window = pg.display.set_mode([700, 700])
pg.display.set_caption("Snake Game")

font = pg.font.SysFont("Lucida Console", 30)

color_black = (0, 0, 0)
color_goldenrod = (218, 165, 32)
color_red = (255, 0, 0)

score = 0