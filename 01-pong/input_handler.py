import pygame 

def handle_events(gameHandler):

  # Check if close button was clicked
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameHandler.is_game_running = False