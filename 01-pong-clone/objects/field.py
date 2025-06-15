import pygame
from pygame.locals import *

class Field:
  def __init__(self, field_config):
    self.game_config = field_config.game_config
    self.width = field_config.width
    self.height = field_config.height
    self.thickness = field_config.thickness
    self.color = field_config.color

    self.top_wall_rect = Rect(0, 0, self.width, self.thickness)
    self.bottom_wall_rect = Rect(0, self.height - self.thickness, self.width, self.thickness)
  
  def render(self, surface):
    self.draw_walls(surface)
    self.draw_dividing_line(surface)
  
  def draw_walls(self, surface):
    # top wall
    pygame.draw.rect(surface, self.color, self.top_wall_rect)

    # bottom wall
    pygame.draw.rect(surface, self.color, self.bottom_wall_rect)
  
  def draw_dividing_line(self, surface):
    pygame.draw.line(surface, self.color, (self.game_config.screen_width / 2, 0), (self.game_config.screen_width / 2, self.game_config.screen_height))

  # def render(self, surface):
  #   # top wall
  #   self.draw_wall(surface, self.color, self.top_wall_rect)
  #   self.draw_wall(surface, self.color, self.bottom_wall_rect)
  #   # self.draw_dividing_line(self, surface)
  
  # def draw_wall(surface, color, rect):
  #   pygame.draw.rect(surface, color, rect)

