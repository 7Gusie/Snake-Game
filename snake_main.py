import sys, random
from snake_assets import pg, window, font, color_black, color_red, color_goldenrod, score

clock = pg.time.Clock()

background = pg.image.load("background.png")
dest = (0, 0)

snake_position = [100, 50]
snake_size = [(100, 50), (90, 50), (80, 50)]

apple_position = [random.randrange(1, 70) * 10, random.randrange(1 , 66) * 10] 
apple_spawn = True

direction = 'RIGHT'
change_to = direction

def showScore(option, color_black, font):
    window.blit(font.render("Pontuação:" + str(score), True, color_black), (0, 668))

def gameOver():
    window.blit(font.render("VOCÊ PERDEU!", True, color_black), (300, 300))
    showScore(1, color_black, font)

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
                change_to = "LEFT"
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                change_to = "RIGHT"
    
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

    snake_size.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 1
        apple_spawn = False
    else:
        snake_size.pop()

    if not apple_spawn:
        apple_position = [random.randrange(1, 70) * 10, random.randrange(1, 70) * 10]
        apple_spawn = True

    window.blit(background, dest)

    for pos in snake_size:
        pg.draw.rect(window, color_goldenrod, pg.Rect(pos[0], pos[1], 10, 10))
        
    pg.draw.rect(window, color_red, pg.Rect(apple_position[0], apple_position[1], 10, 10))
        
    if snake_position[0] < 0 or snake_position[0] > 990:
        gameOver()
    if snake_position[1] < 0 or snake_position[1] > 690:
        gameOver()

    for pixel in snake_size[1:]:
        if snake_position[0] == pixel[0] and snake_position[1] == pixel[1]:
            gameOver()

    showScore(1, color_black, font)

    clock.tick(20)
    pg.display.update()
