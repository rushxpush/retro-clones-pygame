import pygame

color = (255, 255, 0)

def render(gameHandler):
  pygame.draw.rect(gameHandler.surface, color, pygame.Rect(30, 30, 60, 60))
  pygame.display.flip()
