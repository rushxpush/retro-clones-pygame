import pygame
import math
from ui.button import Button
from states.playing_state import PlayingState

class MainMenuState:
  def __init__(self, game_handler, game_config, game_objects):
    self.game_handler = game_handler
    self.game_config = game_config
    self.game_objects = game_objects

    self.font = pygame.font.SysFont("Arial", 16, bold=True)
    self.font_color = (255, 255, 255)

    # TEXT SURFACE
    self.button_1_text_surface = self.font.render("1-Player Game", True, self.font_color)
    self.button_2_text_surface = self.font.render("2-Player Game", True, self.font_color)
    self.button_options_text_surface = self.font.render("Options", True, self.font_color)
    self.button_quit_text_surface = self.font.render("Quit", True, self.font_color)

    self.button_width = self.game_config.screen_width / 3 
    self.button_height = self.game_config.screen_height / 9 

    # BUTTON 1 - PLAYER 1
    self.button_1_x_pos = self.game_config.screen_width / 2 - self.button_width / 2
    self.button_1_y_pos = math.floor(self.button_height * 2)

    self.button_1_rect = pygame.Rect(self.button_1_x_pos, self.button_1_y_pos, self.button_width, self.button_height)
    self.button_start_game_1_player = Button(game_handler, self.button_1_text_surface, self.button_1_rect)

    # BUTTON 2 - PLAYER 2
    self.button_2_x_pos = self.game_config.screen_width / 2 - self.button_width / 2
    self.button_2_y_pos = math.floor(self.button_height * 3)

    self.button_2_rect = pygame.Rect(self.button_2_x_pos, self.button_2_y_pos, self.button_width, self.button_height)
    self.button_start_game_2_player = Button(game_handler, self.button_2_text_surface, self.button_2_rect)

    # BUTTON 3 - OPTIONS
    self.button_options_x_pos = self.game_config.screen_width / 2 - self.button_width / 2
    self.button_options_y_pos = math.floor(self.button_height * 4)

    self.button_options_rect = pygame.Rect(self.button_options_x_pos, self.button_options_y_pos, self.button_width, self.button_height)
    self.button_options = Button(game_handler, self.button_options_text_surface, self.button_options_rect)

    # BUTTON 4 - QUIT
    self.button_quit_x_pos = self.game_config.screen_width / 2 - self.button_width / 2
    self.button_quit_y_pos = math.floor(self.button_height * 5)

    self.button_quit_rect = pygame.Rect(self.button_quit_x_pos, self.button_quit_y_pos, self.button_width, self.button_height)
    self.button_quit = Button(game_handler, self.button_quit_text_surface, self.button_quit_rect)

    # TEXT POSITION
    self.button_1_text_size = self.button_1_text_surface.get_size()
    self.button_2_text_size = self.button_2_text_surface.get_size()
    self.button_options_text_size = self.button_options_text_surface.get_size()
    self.button_quit_text_size = self.button_quit_text_surface.get_size()

    self.button_1_text_pos = center_text(self.button_1_x_pos, self.button_1_y_pos, self.button_width, self.button_height, self.button_1_text_size[0], self.button_1_text_size[1])
    self.button_2_text_pos = center_text(self.button_2_x_pos, self.button_2_y_pos, self.button_width, self.button_height, self.button_2_text_size[0], self.button_2_text_size[1])
    self.button_options_text_pos = center_text(self.button_options_x_pos, self.button_options_y_pos, self.button_width, self.button_height, self.button_options_text_size[0], self.button_options_text_size[1])
    self.button_quit_text_pos = center_text(self.button_quit_x_pos, self.button_quit_y_pos, self.button_width, self.button_height, self.button_quit_text_size[0], self.button_quit_text_size[1])

  def checkState(self):
    None
  
  def handle_events(self):
    keystate = pygame.key.get_pressed()
    isMouseClicked = pygame.mouse.get_pressed()[0]

    # Check if close button was clicked
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_handler.is_game_running = False

    if keystate[pygame.K_ESCAPE]:
      self.game_handler.is_game_running = False

    # Player 1
    # if keystate[pygame.K_w] and not keystate[pygame.K_s]:
    # elif keystate[pygame.K_s] and not keystate[pygame.K_w]:
    # elif keystate[pygame.K_s] and keystate[pygame.K_w]:
    # else:


    # BUTTON 1 HANDLE
    if (self.button_1_rect.collidepoint (pygame.mouse.get_pos())):
      self.button_start_game_1_player.change_bg_color('hover')

      if isMouseClicked:
        self.button_start_game_1_player.change_bg_color('clicked')
        # I have to change this. Maybe pass a variable that says the game is 1 player
        # and the ia should be loaded?
        self.game_handler.current_state = PlayingState(self.game_handler, self.game_objects)

    else:
      self.button_start_game_1_player.change_bg_color('default')
      
    # BUTTON 2 HANDLE 
    if (self.button_2_rect.collidepoint (pygame.mouse.get_pos())):
      self.button_start_game_2_player.change_bg_color('hover')

      if isMouseClicked:
        self.button_start_game_2_player.change_bg_color('clicked')
        self.game_handler.current_state = PlayingState(self.game_handler, self.game_objects)

    else:
      self.button_start_game_2_player.change_bg_color('default')

    # BUTTON 3 OPTIONS HANDLE 
    if (self.button_options_rect.collidepoint (pygame.mouse.get_pos())):
      self.button_options.change_bg_color('hover')

      if isMouseClicked:
        self.button_options.change_bg_color('clicked')

    else:
      self.button_options.change_bg_color('default')

    # BUTTON 4 QUIT HANDLE 
    if (self.button_quit_rect.collidepoint (pygame.mouse.get_pos())):
      self.button_quit.change_bg_color('hover')

      if isMouseClicked:
        self.button_quit.change_bg_color('clicked')
        self.game_handler.is_game_running = False


    else:
      self.button_quit.change_bg_color('default')
  
  def update(self):

    None

  def render(self):
    self.button_start_game_1_player.render()
    self.button_start_game_2_player.render()
    self.button_options.render()
    self.button_quit.render()

    self.game_handler.surface.blit(self.button_1_text_surface, self.button_1_text_pos)
    self.game_handler.surface.blit(self.button_2_text_surface, self.button_2_text_pos)
    self.game_handler.surface.blit(self.button_options_text_surface, self.button_options_text_pos)
    self.game_handler.surface.blit(self.button_quit_text_surface, self.button_quit_text_pos)
    
def center_text(button_pos_x, button_pos_y, button_width, button_height, text_size_x, text_size_y):
  text_pos_x = button_pos_x + (button_width / 2) - (text_size_x / 2)
  text_pos_y = button_pos_y + (button_height / 2) - (text_size_y / 2)
  return (text_pos_x, text_pos_y)