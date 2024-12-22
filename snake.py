import pygame
import time
import random

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

def show_text(text, color, font, size, x, y):
    font_style = pygame.font.SysFont(font, size)
    text_surface = font_style.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    game_window.blit(text_surface, text_rect)

def set_difficulty():
    game_window.fill(black)
    show_text("Select Difficulty", white, 'times new roman', 50, window_x / 2, window_y / 4)
    show_text("1. Easy", white, 'times new roman', 30, window_x / 2, window_y / 2 - 50)
    show_text("2. Medium", white, 'times new roman', 30, window_x / 2, window_y / 2)
    show_text("3. Hard", white, 'times new roman', 30, window_x / 2, window_y / 2 + 50)
    pygame.display.update()

    selecting = True
    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 10
                if event.key == pygame.K_2:
                    return 15
                if event.key == pygame.K_3:
                    return 20

snake_speed = set_difficulty()

snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    show_text("Press Q to Quit or R to Restart", white, 'times new roman', 30, window_x / 2, window_y / 2 + 100)
    pygame.display.flip()

def quit_or_restart():
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    main_game()

def main_game():
    global snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score, snake_speed
    snake_position = [100, 50]
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                      random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True

    direction = 'RIGHT'
    change_to = direction

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
            
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                              random.randrange(1, (window_y//10)) * 10]
            
        fruit_spawn = True
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            game_over()
            quit_or_restart()
        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            game_over()
            quit_or_restart()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
                quit_or_restart()

        show_score(1, white, 'times new roman', 20)
        pygame.display.update()

        fps.tick(snake_speed)

main_game()
