import pygame

color = (255, 255, 0)

def render(game_handler, game_objects):
  game_handler.clearScreen()
  game_objects['player_1'].render(game_handler.surface)
  game_objects['player_2'].render(game_handler.surface)
  game_objects['ball'].render(game_handler.surface)
  game_objects['field'].render(game_handler.surface)

  # DEBUG
  # game_objects['player_1'].render_collision_box(game_handler.surface)
  # game_objects['player_2'].render_collision_box(game_handler.surface)
  # game_objects['ball'].render_collision_box(game_handler.surface)
  pygame.display.flip()


