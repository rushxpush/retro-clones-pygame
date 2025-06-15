import pygame

color = (255, 255, 0)

def render(gameHandler, player, ball):
  gameHandler.clearScreen()
  player.render(gameHandler.surface)
  ball.render(gameHandler.surface)

  # DEBUG
  # ball.render_collision_box(gameHandler.surface)
  # player.render_collision_box(gameHandler.surface)
  pygame.display.flip()


