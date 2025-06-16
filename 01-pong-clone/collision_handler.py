def check_ball_paddle_collision(paddle_position, paddle, ball):
  if (paddle_position == 'left'): 
    if (ball.rect.colliderect(paddle.rect)) and ball.direction_x < 0:
      ball.direction_x *= -1
      ball.speed += 0.2
  elif (paddle_position == 'right'): 
    if (ball.rect.colliderect(paddle.rect)) and ball.direction_x > 0:
      ball.direction_x *= -1
      ball.speed += 0.2