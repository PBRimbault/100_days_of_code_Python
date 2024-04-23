from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self):
        super().__init__()
        self.paddle = Turtle("square")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.turtlesize(stretch_len=5)
        self.paddle.setheading(90)

    def set_paddle(self, position):
        self.paddle.goto(position)        

    def move_up(self):
        self.paddle.forward(MOVE_DISTANCE)

    def move_down(self):
        self.paddle.backward(MOVE_DISTANCE)
