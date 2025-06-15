import pygame

class Ball:
  def __init__(self, game_config, ball_config):
    self.game_config = game_config
    self.x = ball_config.x
    self.y = ball_config.y
    self.radius = ball_config.radius
    self.speed = ball_config.speed
    self.direction_x = ball_config.direction_x
    self.direction_y = ball_config.direction_y
    self.color = ball_config.color
  
  def render(self, surface):
    pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

  def move(self):
    self.x += self.direction_x * self.speed
    self.y += self.direction_y * self.speed

  def handle_collision(self):
    if (self.y - self.radius < 0):
      self.direction_y *= -1
    elif (self.y + self.radius > self.game_config.screen_height):
      self.direction_y *= -1

    
