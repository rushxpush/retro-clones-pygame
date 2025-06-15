import pygame
from input_handler import *
from update import *
from render import *

# Game Loop
def game_loop(gameHandler, player, ball):
  running = True

  while gameHandler.is_game_running:
    HandleEvents(gameHandler, player)
    update(gameHandler, player, ball)
    ball.handle_collision()
    player.handle_collision()
    render(gameHandler, player, ball)

    gameHandler.tick()
  
  pygame.quit()