from setup import *
from game_loop import *
from game_variables import GameVariables

gameHandler = GameVariables()

# Run initialization
initialize_game(gameHandler)

# Runs game loop
game_loop(gameHandler)