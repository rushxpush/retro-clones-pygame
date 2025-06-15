from setup import *
from game_loop import *
from game_variables import GameVariables
from config.paddle_config import InitPaddleConfig
from config.ball_config import InitBallConfig
from config.game_config import InitGameConfig
from objects.paddle import Paddle
from objects.ball import Ball

# Initial config
game_config = InitGameConfig()
player_config = InitPaddleConfig()
ball_config = InitBallConfig(game_config)

gameHandler = GameVariables()
player = Paddle(game_config, player_config)
ball = Ball(game_config, ball_config)

# Run initialization
initialize_game(game_config, gameHandler, player)

# Runs game loop
game_loop(gameHandler, player, ball)