import pygame

color = (255, 255, 0)

def render(gameHandler, player, ball):
  gameHandler.clearScreen()
  player.render(gameHandler.surface)
  ball.render(gameHandler.surface)
  pygame.display.flip()


