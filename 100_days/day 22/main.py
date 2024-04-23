from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('dark green')
screen.title('Pong Game')
screen.tracer(0)

right_paddle = Paddle()
right_paddle.set_paddle((350, 0))

left_paddle = Paddle()
left_paddle.set_paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()





screen.exitonclick()