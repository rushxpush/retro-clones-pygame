import pygame

# Initialization
def initialize_game(game_config, gameHandler, player):
  # Init pygame
  pygame.init()

  # Set screen/surface
  gameHandler.surface = pygame.display.set_mode((game_config.screen_width, game_config.screen_height))
  pygame.display.set_caption("Hello Pygame")
