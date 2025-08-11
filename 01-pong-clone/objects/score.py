import pygame
from pygame.locals import *

class Score:
  def __init__(self):
    self.player_score = {
      'player_1': 0,
      'player_2': 0
    }
    self.point = 1
    None
  
  def increase_score(self, player):
    self.player_score[player] += self.point
  
  def reset_scores(self):
    self.player_score['player_1'] = 0
    self.player_score['player_2'] = 0
