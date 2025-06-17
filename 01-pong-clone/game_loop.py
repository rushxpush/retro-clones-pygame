import pygame
from input_handler import *
from update import *
from render import *

# Game Loop
def game_loop(game_handler, game_objects):
  player_objects = {
    'player_1': game_objects['player_1'],
    'player_2': game_objects['player_2']
  }

  while game_handler.is_game_running:
    HandleEvents(game_handler, player_objects)

    update(game_objects)

    render(game_handler, game_objects)

    game_handler.tick()
  
  pygame.quit()