import pygame
from pygame.locals import *
import struct

class Score:
  def __init__(self, game_handler, game_config):
    self.game_handler = game_handler
    self.game_config = game_config

    self.player_score = {
      'player_1': 0,
      'player_2': 0 
    }
    self.point = 1

    self.font = pygame.font.SysFont("Arial", 22, bold=True)
    self.font_color = (255, 255, 255)
    self.score_distance_from_center = 20

    self.player_1_score_surface = self.font.render(str(self.player_score['player_1']), True, self.font_color)
    self.player_2_score_surface = self.font.render(str(self.player_score['player_2']), True, self.font_color)

  def render(self):
    self.game_handler.surface.blit(self.player_1_score_surface, (self.game_config.screen_width / 2 - self.get_text_center_point(self.player_1_score_surface)['x'] / 2 - self.score_distance_from_center, 20))
    self.game_handler.surface.blit(self.player_2_score_surface, (self.game_config.screen_width / 2 - self.get_text_center_point(self.player_1_score_surface)['x'] / 2 + self.score_distance_from_center, 20))

    None
  
  def increase_score(self, player):
    self.player_score[player] += self.point
    self.player_1_score_surface = self.font.render(str(self.player_score['player_1']), True, self.font_color)
    self.player_2_score_surface = self.font.render(str(self.player_score['player_2']), True, self.font_color)
  
  def reset_scores(self):
    self.player_score['player_1'] = 0
    self.player_score['player_2'] = 0
  
  def get_text_center_point(self, text_surface):
    size = text_surface.get_size()
    return {
      'x': size[0],
      'y': size[1]
    }

