import sys, random, pygame as pg

pg.init()
pg.font.init()

window = pg.display.set_mode([1200, 900])
pg.display.set_caption("Snake Game")

font = pg.font.SysFont("Lucida Console", 30)

clock = pg.time.Clock()

color_indigo = (75, 0, 130)

snake_position = [600, 450]
snake_size = [(100, 50), (90, 50), (80, 50)]

apple_position = [random.randrange(1, 120 * 10), random.randrange(1 , 90 * 10)] 
apple_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def showScore():
    showScore_surface = font.render("Pontuação: " + str(score), True, color_indigo)
    window.blit(showScore_surface, (200, 200))


def gameOver():
    gameOver_text = font.render("VOCÊ PERDEU!", True, color_indigo)
    window.blit(gameOver_text, (300, 300))
    showScore()

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w or event.key == pg.K_UP:
                    change_to = "UP"
                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    change_to = "DOWN"
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    change_to = "UP"
                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    change_to = "DOWN"
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == "UP":
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        clock.tick(60)
        pg.display.update()

main()
