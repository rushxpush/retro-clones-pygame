def check_ball_paddle_collision(ball, paddle):
  if (ball.rect.colliderect(paddle.rect)) and ball.direction_x < 0:
    ball.direction_x *= -1
    ball.speed += 0.2