import pygame, sys, time, random

mode = input("game or demo?")
difficulty = 50

# Window size
width = 600
height = 600


check_errors = pygame.init()


w = 10

pygame.display.set_caption('Snake Eater')
display = pygame.display.set_mode((width, height))

background = (27, 79, 114)
white = (236, 240, 241)
yellow = (241, 196, 15)
darkYellow = (247, 220, 111)
red = (231, 76, 60)
darkRed = (241, 148, 138)
darkBlue = (40, 116, 166)

fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

x1 = 1
y1 = 0

score = 0

def draw_grids():
    squares = 50
    for i in range(width // squares):
        pygame.draw.line(display, darkBlue, (i * squares, 0), (i * squares, height))
        pygame.draw.line(display, darkBlue, (0, i * squares), (width, i * squares))



def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (int(width/2), int(height/4))
    display.fill(background)
    draw_grids()
    display.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (int(width/10), 15)
    else:
        score_rect.midtop = (int(width/2), int(height/1.25))
    display.blit(score_surface, score_rect)
    # pygame.display.flip()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if not (x1 == 0 and y1 == 1):
                    x1 = 0
                    y1 = -1
            if event.key == pygame.K_s:
                if not (x1 == 0 and y1 == -1):
                    x1 = 0
                    y1 = 1
            if event.key == pygame.K_a:
                if not (x1 == 1 and y1 == 0):
                    x1 = -1
                    y1 = 0
            if event.key == pygame.K_d:
                if not (x1 == -1 and y1 == 0):
                    x1 = 1
                    y1 = 0
    if mode == "game":
        if x1 == 0 and y1 == -1:
            snake_pos[1] -= 10
        if x1 == 0 and y1 == 1:
            snake_pos[1] += 10
        if x1 == -1 and y1 == 0:
            snake_pos[0] -= 10
        if x1 == 1 and y1 == 0:
            snake_pos[0] += 10
    elif mode == "demo":

        right = True
        for block in snake_body[1:]:
            if snake_pos[0] + 10 == block[0] and snake_pos[1] == block[1]:
                right = False
        left = True
        for block in snake_body[1:]:
            if snake_pos[0] - 10 == block[0] and snake_pos[1] == block[1]:
                left = False
        up = True
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] - 10 == block[1]:
                up = False
        down = True
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] + 10 == block[1]:
                down = False

        if food_pos[0] > snake_pos[0] and food_pos[1] > snake_pos[1]:
            if right:
                snake_pos[0] += 10
            elif down:
                snake_pos[1] += 10
            elif left:
                snake_pos[0] -= 10
            elif up:
                snake_pos[1] -= 10
        elif food_pos[0] > snake_pos[0] and food_pos[1] < snake_pos[1]:
            if right:
                snake_pos[0] += 10
            elif up:
                snake_pos[1] -= 10
            elif down:
                snake_pos[1] += 10
            elif left:
                snake_pos[0] -= 10
        elif food_pos[0] < snake_pos[0] and food_pos[1] < snake_pos[1]:
            if left:
                snake_pos[0] -= 10
            elif up:
                snake_pos[1] -= 10
            elif down:
                snake_pos[1] += 10
            elif right:
                snake_pos[0] += 10
        elif food_pos[0] < snake_pos[0] and food_pos[1] > snake_pos[1]:
            if left:
                snake_pos[0] -= 10
            elif down:
                snake_pos[1] += 10
            elif up:
                snake_pos[1] -= 10
            elif right:
                snake_pos[0] += 10
        elif food_pos[0] == snake_pos[0] and food_pos[1] > snake_pos[1]:
            if down:
                snake_pos[1] += 10
            elif left:
                snake_pos[0] -= 10
            elif right:
                snake_pos[0] += 10
            elif up:
                snake_pos[1] -= 10
        elif food_pos[0] == snake_pos[0] and food_pos[1] < snake_pos[1]:
            if up:
                snake_pos[1] -= 10
            elif left:
                snake_pos[0] -= 10
            elif right:
                snake_pos[0] += 10
            elif down:
                snake_pos[1] += 10
    #     elif event.type == pygame.KEYDOWN:
    #         # W -> Up; S -> Down; A -> Left; D -> Right
    #         if event.key == pygame.K_UP or event.key == ord('w'):
    #             change_to = 'UP'
    #         if event.key == pygame.K_DOWN or event.key == ord('s'):
    #             change_to = 'DOWN'
    #         if event.key == pygame.K_LEFT or event.key == ord('a'):
    #             change_to = 'LEFT'
    #         if event.key == pygame.K_RIGHT or event.key == ord('d'):
    #             change_to = 'RIGHT'
    #         # Esc -> Create event to quit the game
    #         if event.key == pygame.K_ESCAPE:
    #             pygame.event.post(pygame.event.Event(pygame.QUIT))
    #
    # # Making sure the snake cannot move in the opposite direction instantaneously
    # if change_to == 'UP' and direction != 'DOWN':
    #     direction = 'UP'
    # if change_to == 'DOWN' and direction != 'UP':
    #     direction = 'DOWN'
    # if change_to == 'LEFT' and direction != 'RIGHT':
    #     direction = 'LEFT'
    # if change_to == 'RIGHT' and direction != 'LEFT':
    #     direction = 'RIGHT'
    #
    # # Moving the snake
    # if direction == 'UP':
    #     snake_pos[1] -= 10
    # if direction == 'DOWN':
    #     snake_pos[1] += 10
    # if direction == 'LEFT':
    #     snake_pos[0] -= 10
    # if direction == 'RIGHT':
    #     snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()


    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # GFX
    display.fill(background)
    draw_grids()
    for pos in snake_body:
        pygame.draw.rect(display, red, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(display, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))


    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        print("a")
        game_over()

    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        print("b")
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            print("c")
            game_over()

    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)
