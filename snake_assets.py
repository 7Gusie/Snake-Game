from logging.config import RESET_ERROR
import os, time, pygame as pg

pg.init()
pg.font.init()

window = pg.display.set_mode([700, 700])
pg.display.set_caption("Snake Game")

font = pg.font.SysFont("Lucida Console", 30)

background = pg.image.load("assets/background.png")
background_gameOver = pg.image.load("assets/background_gameOver.png")
background_position = (0, 0)

color_white = (255, 255, 255)
color_goldenrod = (218, 165, 32)
color_red = (255, 0, 0)

score = 0

def backgroundScreen():
    window.blit(background, background_position)

def background_gameOver_Screen():
    window.blit(background_gameOver, background_position)

def showScore(score):
    window.blit(font.render("Pontuação:" + str(score), True, color_white), (0, 670))
    window.blit(font.render("ESC para sair", True, color_white), (465, 670))

def cleanScreen():
    os.system("cls")

def writeScreen(text):
    print(text)