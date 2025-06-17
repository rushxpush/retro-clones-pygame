def check_ball_paddle_collision(paddle_position, paddle, ball):
  if (paddle_position == 'left'): 
    if (ball.rect.colliderect(paddle.rect)) and ball.direction_x < 0:
      ball.direction_x *= -1
      ball.speed += 0.2
  elif (paddle_position == 'right'): 
    if (ball.rect.colliderect(paddle.rect)) and ball.direction_x > 0:
      ball.direction_x *= -1
      ball.speed += 0.2

def check_collisions(game_objects):
  game_objects['player_1'].handle_collision()
  game_objects['player_2'].handle_collision()
  game_objects['ball'].handle_collision()

  check_ball_paddle_collision('left', game_objects['player_1'], game_objects['ball'])
  check_ball_paddle_collision('right', game_objects['player_2'], game_objects['ball'])