class InitPaddleConfig:
  def __init__(self, game_handler, game_config):
    self.game_handler = game_handler
    self.game_config = game_config
    self.x = 10
    self.y = 10
    self.width = 10
    self.height = 30
    self.color = (255, 255, 255)

    self.direction = 0
    self.normal_speed = 4 
    self.fast_speed = 6