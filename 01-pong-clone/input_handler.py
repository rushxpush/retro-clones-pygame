import pygame 

def HandleEvents(game_handler, player_objects):
  keystate = pygame.key.get_pressed()

  # Check if close button was clicked
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_handler.is_game_running = False



  if keystate[pygame.K_ESCAPE]:
    game_handler.is_game_running = False

  # Player 1
  if keystate[pygame.K_w] and not keystate[pygame.K_s]:
    player_objects['player_1'].set_direction(-1)
  elif keystate[pygame.K_s] and not keystate[pygame.K_w]:
    player_objects['player_1'].set_direction(1)
  elif keystate[pygame.K_s] and keystate[pygame.K_w]:
    player_objects['player_1'].set_direction(1)
  else:
    player_objects['player_1'].set_direction(0)

  # Player 2 
  if keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
    player_objects['player_2'].set_direction(-1)
  elif keystate[pygame.K_DOWN] and not keystate[pygame.K_UP]:
    player_objects['player_2'].set_direction(1)
  elif keystate[pygame.K_DOWN] and keystate[pygame.K_UP]:
    player_objects['player_2'].set_direction(1)
  else:
    player_objects['player_2'].set_direction(0)


