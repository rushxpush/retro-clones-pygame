class InitFieldConfig:
  def __init__(self, game_handler, game_config):
    self.game_handler = game_handler
    self.game_config = game_config
    self.width = game_config.screen_width
    self.height = game_config.screen_height
    self.thickness = 5
    self.color = (255, 255, 255)
