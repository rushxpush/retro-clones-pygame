import pygame

color = (255, 255, 0)

def render(gameHandler, game_objects):
  gameHandler.clearScreen()
  game_objects['player_1'].render(gameHandler.surface)
  game_objects['player_2'].render(gameHandler.surface)
  game_objects['ball'].render(gameHandler.surface)
  game_objects['field'].render(gameHandler.surface)

  # DEBUG
  # game_objects['player_1'].render_collision_box(gameHandler.surface)
  # game_objects['player_2'].render_collision_box(gameHandler.surface)
  # game_objects['ball'].render_collision_box(gameHandler.surface)
  pygame.display.flip()


