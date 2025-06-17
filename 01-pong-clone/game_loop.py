import pygame
from input_handler import *
from update import *
from render import *
from collision_handler import check_ball_paddle_collision

# Game Loop
def game_loop(gameHandler, game_objects):
  player_objects = {
    'player_1': game_objects['player_1'],
    'player_2': game_objects['player_2']
  }


  while gameHandler.is_game_running:
    HandleEvents(gameHandler, player_objects)

    update(game_objects)
    game_objects['player_1'].handle_collision()
    game_objects['player_2'].handle_collision()
    game_objects['ball'].handle_collision()
    check_ball_paddle_collision('left', game_objects['player_1'], game_objects['ball'])
    check_ball_paddle_collision('right', game_objects['player_2'], game_objects['ball'])

    render(gameHandler, game_objects)

    gameHandler.tick()
  
  pygame.quit()