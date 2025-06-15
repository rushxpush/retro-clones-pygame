class InitBallConfig:
  def __init__(self, game_handler, game_config):
    self.game_handler = game_handler
    self.game_config = game_config
    self.x = game_config.screen_width / 2
    self.y = game_config.screen_height / 2
    self.radius = 5
    self.speed = 2 
    self.direction_x = -1
    # self.direction_y = -1
    self.direction_y = 0
    self.color = (255, 255, 255)

