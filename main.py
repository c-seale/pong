import pygame

from object.ball import Ball
from object.goal import Goal
from object.paddle import Paddle
from play_arena import PlayArena


def main():
    # CONFIG
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    SCREEN_COLOR_BACKGROUND = pygame.Color('WHITE')
    SCREEN_BORDER_WIDTH = 20
    SCREEN_BORDER_COLOR = pygame.Color('BLACK')
    BALL_RADIUS = 10
    BALL_COLOR = pygame.Color('RED')
    BALL_SPEED = 3
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 200
    PADDLE_COLOR = pygame.Color('BLUE')
    PADDLE_SPEED = 5
    FPS_LIMIT = 120

    # os.environ['SDL_VIDEO_CENTERED'] = '1'  # App opens centered on screen

    pygame.init()
    primary_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('cseale\'s Pong!')
    game_clock = pygame.time.Clock()

    # Initialize starting objects
    arena = PlayArena(primary_surface, SCREEN_COLOR_BACKGROUND, SCREEN_BORDER_WIDTH, SCREEN_BORDER_COLOR)
    active_ball = reset_ball(primary_surface, BALL_RADIUS, BALL_SPEED, BALL_COLOR)
    player_one_paddle = reset_player_one(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)
    player_two_paddle = reset_player_two(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)

    player_one_score = 0
    player_two_score = 0

    running = True
    while running:
        scored = False

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # Handle input
        pressed_keys = pygame.key.get_pressed()

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
            scored = True
            if collided_obj.name == 'right':
                player_one_score += 1
            elif collided_obj.name == 'left':
                player_two_score += 1
            else:
                return NotImplementedError

        pygame.display.flip()  # refresh display

        if scored:  # reset players and ball
            pygame.time.delay(500)
            active_ball = reset_ball(primary_surface, BALL_RADIUS, BALL_SPEED, BALL_COLOR)
            player_one_paddle = reset_player_one(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)
            player_two_paddle = reset_player_two(primary_surface, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_COLOR)

        game_clock.tick(FPS_LIMIT)

    pygame.quit()


def reset_player_one(surface, paddle_width, paddle_height, paddle_color):
    return Paddle(surface, paddle_width, surface.get_height() // 2 - paddle_height // 2, 0, paddle_width, paddle_height,
                  paddle_color)


def reset_player_two(surface, paddle_width, paddle_height, paddle_color):
    return Paddle(surface, surface.get_width() - 2 * paddle_width, surface.get_height() // 2 - paddle_height // 2, 0,
                  paddle_width, paddle_height, paddle_color)


def reset_ball(surface, ball_radius, ball_seed, ball_color):
    return Ball(surface, surface.get_width() // 2, surface.get_height() // 2, -ball_seed, 0, ball_radius, ball_color)


if __name__ == '__main__':
    main()
