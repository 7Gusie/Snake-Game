import pygame as pg, sys

pg.init()
pg.font.init()

window = pg.display.set_mode([1200, 900], pg.RESIZABLE)
pg.display.set_caption("Snake Game")

font = pg.font.SysFont('Lucida Console', 30)

color_indigo = (75, 0, 130)

clock = pg.time.Clock()

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        clock.tick(60)
        pg.display.update()

main()