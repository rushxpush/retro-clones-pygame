from setup import *
from game_loop import *
from game_variables import GameVariables

from config.paddle_config import InitPaddleConfig
from config.ball_config import InitBallConfig
from config.game_config import InitGameConfig

from objects.paddle import Paddle
from objects.ball import Ball

# Initialization
game_handler = GameVariables()
game_config = InitGameConfig()
initialize_game(game_handler, game_config)

# Objects config
player_config = InitPaddleConfig(game_handler, game_config)
ball_config = InitBallConfig(game_handler, game_config)

player = Paddle(player_config)
ball = Ball(ball_config)

game_objects = {
  'player': player,
  'ball': ball
}

# Runs game loop
game_loop(game_handler, game_objects)