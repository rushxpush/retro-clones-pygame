import pygame

# Initialization
def initialize_game(gameHandler):
  # Init pygame
  pygame.init()

  # Set screen/surface
  gameHandler.surface = pygame.display.set_mode((400, 300))
  pygame.display.set_caption("Hello Pygame")
