import pygame

class Paddle:
  def __init__(self):
    self.x = None 
    self.y = None 
    self.width = 10
    self.height = 30
    self.color = (255, 255, 255)

    self.direction = 0
    self.normal_speed = 4 
    self.fast_speed = 6

    self.last_key_pressed = None
  
  def set_direction(self, direction):
    self.direction = direction

  def move(self):
    self.y += self.direction * self.normal_speed

  # def 


  def render(self, surface):
    pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))