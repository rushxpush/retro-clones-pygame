import pygame 

def HandleEvents(gameHandler, player):

  # Check if close button was clicked
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameHandler.is_game_running = False

  keystate = pygame.key.get_pressed()

  if keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
    player.set_direction(-1)
  elif keystate[pygame.K_DOWN] and not keystate[pygame.K_UP]:
    player.set_direction(1)
  elif keystate[pygame.K_DOWN] and keystate[pygame.K_UP]:
    player.set_direction(1)
  else:
    player.set_direction(0)
