import pygame
from pygame.locals import *

class Paddle:
  def __init__(self, player_config):
    self.game_config = player_config.game_config
    self.x = player_config.x 
    self.y = player_config.y 
    self.width = player_config.width
    self.height = player_config.height
    self.color = player_config.color 

    self.direction = player_config.direction
    self.normal_speed = player_config.normal_speed
    self.fast_speed = player_config.fast_speed

    self.rect = Rect(self.x, self.y, self.width, self.height)

    self.last_key_pressed = None

  def render(self, surface):
    pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

  def render_collision_box(self, surface):
    pygame.draw.rect(surface, (0, 255, 0), self.rect)
  
  def set_direction(self, direction):
    self.direction = direction

  def move(self):
    self.y += self.direction * self.normal_speed
    
    self.rect.y += self.direction * self.normal_speed

  def update_collision_box(self):
    self.rect.x = self.x
    self.rect.y = self.y

  def handle_collision(self):
    if self.y < 0:
      self.y = 0
    elif self.y + self.height > self.game_config.screen_height:
      self.y = self.game_config.screen_height - self.height 
