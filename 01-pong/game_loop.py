import pygame
from input_handler import *
from update import *
from render import *

# Game Loop
def game_loop(gameHandler):
  running = True

  while gameHandler.is_game_running:
    handle_events(gameHandler)
    update(gameHandler)
    render(gameHandler)

    gameHandler.tick()
  
  pygame.quit()