import pygame
from input_handler import *
from update import *
from render import *
from collision_handler import check_ball_paddle_collision

# Game Loop
def game_loop(gameHandler, game_objects):
  running = True

  while gameHandler.is_game_running:
    HandleEvents(gameHandler, game_objects['player'])
    update(gameHandler, game_objects['player'], game_objects['ball'])
    game_objects['player'].handle_collision()
    game_objects['ball'].handle_collision()
    check_ball_paddle_collision(game_objects['player'], game_objects['ball'])

    render(gameHandler, game_objects['player'], game_objects['ball'])

    gameHandler.tick()
  
  pygame.quit()