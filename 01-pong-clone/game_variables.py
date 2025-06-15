import pygame

class GameVariables:
  def __init__(self):
    self.surface = None
    self.fillColor = (0, 0, 0)

    self.is_game_running = True
    self.clock = pygame.time.Clock()
    self.fps = 60
  
  def tick(self):
    self.clock.tick(self.fps)

  def clearScreen(self):
    self.surface.fill(self.fillColor)