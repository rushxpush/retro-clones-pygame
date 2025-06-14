import pygame

class GameVariables:
  def __init__(self):
    self.surface = None

    self.is_game_running = True
    self.clock = pygame.time.Clock()
    self.fps = 60
  
  def tick(self):
    self.clock.tick(self.fps)