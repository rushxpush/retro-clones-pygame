from setup import *
from game_loop import *
from game_variables import GameVariables

from config.game_config import GameConfig
from config.player_1_config import Player1Config
from config.player_2_config import Player2Config
from config.ball_config import BallConfig
from config.field_config import FieldConfig

from objects.paddle import Paddle
from objects.ball import Ball
from objects.field import Field

from states.playing_state import PlayingState
from states.main_menu_state import MainMenuState

# Initialization
game_handler = GameVariables()
game_config = GameConfig()
initialize_game(game_handler, game_config)

# Objects config
player_1_config = Player1Config(game_handler, game_config)
player_2_config = Player2Config(game_handler, game_config)
ball_config = BallConfig(game_handler, game_config)
field_config = FieldConfig(game_handler, game_config)

# Instantiate objects
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

# Init Game States
# game_handler.current_state = PlayingState(game_handler, game_objects)
game_handler.current_state = MainMenuState(game_handler, game_config, game_objects)

# Runs game loop
game_loop(game_handler)