import pygame
from pygame.locals import *

class Ball:
  def __init__(self, ball_config):
    self.game_config = ball_config.game_config
    self.start_pos_x = ball_config.x
    self.start_pos_y = ball_config.y
    self.x = ball_config.x
    self.y = ball_config.y
    self.radius = ball_config.radius
    self.speed = ball_config.speed
    self.direction_x = ball_config.direction_x
    self.direction_y = ball_config.direction_y
    self.color = ball_config.color
    self.rect = Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
  
  def render(self, surface):
    pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
  
  def render_collision_box(self, surface):
    pygame.draw.rect(surface, (255, 0, 0), (self.rect.x, self.rect.y, self.radius * 2, self.radius * 2))
  
  def get_rect(self):
    return self.rect

  def move(self):
    # update position
    self.x += self.direction_x * self.speed
    self.y += self.direction_y * self.speed

    self.update_collision_box()
  
  def set_position(self, pos_x, pos_y):
    self.x = pos_x
    self.y = pos_y
  
  def update_collision_box(self):
    self.rect.x = self.x - self.radius
    self.rect.y = self.y - self.radius

  def handle_collision(self):
    if (self.y - self.radius < 0):
      self.direction_y *= -1
    elif (self.y + self.radius > self.game_config.screen_height):
      self.direction_y *= -1

    
