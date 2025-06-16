from setup import *
from game_loop import *
from game_variables import GameVariables

from config.game_config import InitGameConfig
from config.player_1_config import Player1Config
from config.player_2_config import Player2Config
from config.ball_config import InitBallConfig
from config.field_config import InitFieldConfig

from objects.paddle import Paddle
from objects.ball import Ball
from objects.field import Field

# Initialization
game_handler = GameVariables()
game_config = InitGameConfig()
initialize_game(game_handler, game_config)

# Objects config
player_1_config = Player1Config(game_handler, game_config)
player_2_config = Player2Config(game_handler, game_config)
ball_config = InitBallConfig(game_handler, game_config)
field_config = InitFieldConfig(game_handler, game_config)

player_1 = Paddle(player_1_config)
player_2 = Paddle(player_2_config)
ball = Ball(ball_config)
field = Field(field_config)

game_objects = {
  'player_1': player_1,
  'player_2': player_2,
  'ball': ball,
  'field': field
}

# Runs game loop
game_loop(game_handler, game_objects)