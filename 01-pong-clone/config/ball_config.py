class BallConfig:
  def __init__(self, game_handler, game_config):
    self.game_handler = game_handler
    self.game_config = game_config

    self.radius = 5

    self.x = game_config.screen_width / 2
    self.y = game_config.screen_height / 2 - self.radius

    self.speed = 3 
    self.direction_x = -1
    self.direction_y = -1
    # self.direction_y = 0
    self.color = (255, 255, 255)

