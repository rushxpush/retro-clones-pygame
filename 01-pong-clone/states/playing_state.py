import pygame
from collision_handler import check_collisions

class PlayingState:
  def __init__(self,game_handler, game_objects):
    self.game_handler = game_handler
    self.game_objects = game_objects
    self.player_objects = {
      'player_1': game_objects['player_1'],
      'player_2': game_objects['player_2']
    }
    
  def handle_events(self):
    keystate = pygame.key.get_pressed()

    # Check if close button was clicked
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_handler.is_game_running = False

    if keystate[pygame.K_ESCAPE]:
      self.game_handler.is_game_running = False

    # Player 1
    if keystate[pygame.K_w] and not keystate[pygame.K_s]:
      self.player_objects['player_1'].set_direction(-1)
    elif keystate[pygame.K_s] and not keystate[pygame.K_w]:
      self.player_objects['player_1'].set_direction(1)
    elif keystate[pygame.K_s] and keystate[pygame.K_w]:
      self.player_objects['player_1'].set_direction(1)
    else:
      self.player_objects['player_1'].set_direction(0)

    # Player 2 
    if keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
      self.player_objects['player_2'].set_direction(-1)
    elif keystate[pygame.K_DOWN] and not keystate[pygame.K_UP]:
      self.player_objects['player_2'].set_direction(1)
    elif keystate[pygame.K_DOWN] and keystate[pygame.K_UP]:
      self.player_objects['player_2'].set_direction(1)
    else:
      self.player_objects['player_2'].set_direction(0)


  def update(self):
    self.move_objects()
    check_collisions(self.game_objects)

  def move_objects(self):
    self.game_objects['player_1'].move()
    self.game_objects['player_2'].move()
    self.game_objects['ball'].move()

  def render(self):
    self.game_handler.clearScreen()
    self.game_objects['player_1'].render(self.game_handler.surface)
    self.game_objects['player_2'].render(self.game_handler.surface)
    self.game_objects['ball'].render(self.game_handler.surface)
    self.game_objects['field'].render(self.game_handler.surface)

    # DEBUG
    # self.game_objects['player_1'].render_collision_box(game_handler.surface)
    # self.game_objects['player_2'].render_collision_box(game_handler.surface)
    # self.game_objects['ball'].render_collision_box(game_handler.surface)
    pygame.display.flip()