import pygame

class Button:
  def __init__(self, game_handler, text, rect):
    self.game_handler = game_handler
    self.color_default = (180, 180, 180)
    self.color_hover = (100, 100, 100)
    self.color_clicked = (100, 255, 100)
    self.color_current = self.color_default
    self.button_state = 'default'
    self.text = text
    self.rect = rect
    None

  def render(self):
    pygame.draw.rect(self.game_handler.surface, self.color_current, self.rect)
  
  def change_bg_color(self, state):
    if state == 'hover' and self.button_state != 'hover':
        self.color_current = self.color_hover
        self.button_state = 'hover'
    elif state == 'default' and self.button_state != 'default':
        self.color_current = self.color_default
        self.button_state = 'default'
    # Having clicked state apart from the hover if could cause problems
    elif state == 'clicked' and self.button_state != 'clicked':
        self.color_current = self.color_clicked
        self.button_state = 'clicked'