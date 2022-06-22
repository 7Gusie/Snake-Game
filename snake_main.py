import sys, random
from snake_assets import pg, window, font, color_black, color_goldenrod, color_red, score, showScore, cleanScreen, writeScreen

clock = pg.time.Clock()

background = pg.image.load("assets/background.png")
background_gameOver = pg.image.load("assets/background_gameOver.png")
background_position = (0, 0)

snake_position = [340, 340]
snake_size = [10]
snake_speed = 10

def gameOver():
    window.blit(background_gameOver, background_position)
    window.blit(font.render("Restart - Pressione 1", True, color_black), (153, 270))
    window.blit(font.render("Quit - Pressione 2", True, color_black), (185, 300))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                gameMain(score)
            if event.key == pg.K_2:
                pg.quit()
                sys.exit()

def gameMain(score):
    apple_position = [random.randrange(1, 70) * 10, random.randrange(1 , 64) * 10] 
    apple_spawn = True

    direction = ''
    change_to = direction

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
            apple_position = [random.randrange(1, 70) * 10, random.randrange(1, 64) * 10]
            apple_spawn = True
            
        window.blit(background, background_position)

        for pos in snake_size:
            pg.draw.rect(window, color_goldenrod, pg.Rect(pos[0], pos[1], 10, 10))
            
        pg.draw.rect(window, color_red, pg.Rect(apple_position[0], apple_position[1], 10, 10))
            
        if snake_position[0] < 0:
            snake_position[0] = 700
        if snake_position[0] > 700: 
            snake_position[0] = 0
        if snake_position[1] < 0:
            snake_position[1] = 700  
        if snake_position[1] > 700:
            snake_position[1] = 0

        for pixel in snake_size[1:]:
            if snake_position[0] == pixel[0] and snake_position[1] == pixel[1]:
                gameOver()

        showScore(score)

        clock.tick(snake_speed)
        pg.display.update()

gameMain(score)
'''
while True:
    try:
        cleanScreen()
        user = input("Usuário: ").title()
        if len(user) > 1:
            while True:
                try:
                    cleanScreen()
                    writeScreen(f'Usuário: {user}')
                    email = input("E-mail: ")
                    if "@" in email and len(email) > 1:
                        player_file = (f'Usuário: {user} - E-mail: {email}')
                        file = open("snake_users.txt", "a")
                        file.write(player_file)
                        file.close()
                        restartGame(score)
                except ValueError:
                    writeScreen(ValueError)
    except ValueError:
        writeScreen(ValueError)
'''