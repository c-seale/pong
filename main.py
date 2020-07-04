import os

import pygame

from object.arena import Arena
from object.ball import Ball
from object.goal import Goal
from object.paddle import Paddle


def main():
    # CONFIG
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    SCREEN_BACKGROUND_COLOR = pygame.Color('WHITE')

    WALL_SIZE = round(SCREEN_HEIGHT * 0.013)
    WALL_COLOR = pygame.Color('BLACK')

    BALL_RADIUS = round(WALL_SIZE * 1.5)
    BALL_COLOR = pygame.Color('RED')
    BALL_SPEED = round(SCREEN_WIDTH * 0.0029)

    PADDLE_WIDTH = round(WALL_SIZE * 1.5)
    PADDLE_HEIGHT = round(SCREEN_HEIGHT * 0.15)
    PADDLE_COLOR = pygame.Color('BLUE')
    PADDLE_SPEED = round(SCREEN_HEIGHT * 0.0065)

    FPS_LIMIT = 120

    os.environ['SDL_VIDEO_CENTERED'] = '1'  # App opens centered on screen

    # Init pygame
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    # Init game window
    primary_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('cseale\'s Pong!')
    game_clock = pygame.time.Clock()

    # Init starting objects
    arena = Arena(primary_surface, SCREEN_BACKGROUND_COLOR, WALL_SIZE, WALL_COLOR)
    active_ball = reset_ball(primary_surface, BALL_RADIUS, BALL_SPEED, BALL_COLOR)
    player_one_paddle = reset_player_one(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)
    player_two_paddle = reset_player_two(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)

    # Init scores
    player_one_score = 0
    player_two_score = 0

    # Init music
    pygame.mixer.music.load(r'sound\bgm-1.mp3')
    pygame.mixer.music.play(-1)

    running = True
    while running:
        # Get active input
        pressed_keys = pygame.key.get_pressed()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and (
                    pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT])):
                running = False
                break

        # process player 1 input
        player_one_paddle.dy = 0
        if pressed_keys[pygame.K_w]:
            player_one_paddle.dy = -PADDLE_SPEED
        if pressed_keys[pygame.K_s]:
            player_one_paddle.dy = PADDLE_SPEED

        # process player 2 input
        player_two_paddle.dy = 0
        if pressed_keys[pygame.K_UP]:
            player_two_paddle.dy = -PADDLE_SPEED
        if pressed_keys[pygame.K_DOWN]:
            player_two_paddle.dy = PADDLE_SPEED

        # Update game state
        arena.update(player_one_score, player_two_score)
        player_one_paddle.update(arena.walls)
        player_two_paddle.update(arena.walls)
        collided_obj = active_ball.update([player_one_paddle, player_two_paddle] + arena.walls + arena.goals)
        if type(collided_obj) == Goal:  # detect scoring
            if collided_obj.name == 'right':
                player_one_score += 1
                ball_speed = abs(BALL_SPEED)
            elif collided_obj.name == 'left':
                player_two_score += 1
                ball_speed = -abs(BALL_SPEED)
            else:
                return NotImplementedError

            pygame.time.delay(500)
            active_ball = reset_ball(primary_surface, BALL_RADIUS, ball_speed, BALL_COLOR)
            player_one_paddle = reset_player_one(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)
            player_two_paddle = reset_player_two(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)

        pygame.display.flip()
        game_clock.tick(FPS_LIMIT)

    pygame.quit()


def reset_player_one(surface, paddle_width, paddle_height, paddle_color):
    return Paddle('p1', surface, paddle_width, surface.get_height() // 2 - paddle_height // 2, 0, paddle_width,
                  paddle_height, paddle_color)


def reset_player_two(surface, paddle_width, paddle_height, paddle_color):
    return Paddle('p2', surface, surface.get_width() - 2 * paddle_width, surface.get_height() // 2 - paddle_height // 2,
                  0, paddle_width, paddle_height, paddle_color)


def reset_ball(surface, ball_radius, ball_seed, ball_color):
    return Ball(surface, surface.get_width() // 2, surface.get_height() // 2, -ball_seed, 0, ball_radius, ball_color)


if __name__ == '__main__':
    main()
