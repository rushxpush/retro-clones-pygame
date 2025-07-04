import pygame

def game_loop(game_handler):

  while game_handler.is_game_running:
    game_handler.current_state.handle_events()
    game_handler.current_state.update()
    game_handler.current_state.render()
    game_handler.tick()
  
  pygame.quit()