import sys, random
from snake_assets import pg, window, font, color_indigo, score

clock = pg.time.Clock()

black = (0, 0, 0)

snake_position = [600, 450]
snake_size = [(100, 50), (90, 50), (80, 50)]

apple_position = [random.randrange(1, 100) * 10, random.randrange(1 , 70) * 10] 
apple_spawn = True

direction = 'RIGHT'
change_to = direction

def showScore(option, color_indigo, font):
    window.blit(font.render("Pontuação: " + str(score), True, color_indigo), (10, 10))

def gameOver():
    window.fill(black)
    window.blit(font.render("VOCÊ PERDEU!", True, color_indigo), (300, 300))
    showScore(1, color_indigo, font)

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

    snake_size.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[1] == apple_position[1]:
        score += 1
        apple_spawn = False
    else:
        snake_size.pop()

    if not apple_spawn:
        apple_position = [random.randrange(1, 100) * 10, random.randrange(1, 70) * 10]
        apple_spawn = True

    window.fill(black)
    for pos in snake_size:
        pg.draw.rect(window, color_indigo, pg.Rect(pos[0], pos[1], 10, 10))
        
    pg.draw.rect(window, color_indigo, pg.Rect(apple_position[0], apple_position[1], 10, 10))
        
    if snake_position[0] < 0 or snake_position[0] > 990:
        gameOver()
    if snake_position[1] < 0 or snake_position[1] > 690:
        gameOver()

    for block in snake_size[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            gameOver()

    showScore(1, color_indigo, font)

    clock.tick(20)
    pg.display.update()
