from collision_handler import check_collisions

def update(game_objects):
  move_objects(game_objects)
  check_collisions(game_objects)

def move_objects(game_objects):
  game_objects['player_1'].move()
  game_objects['player_2'].move()
  game_objects['ball'].move()