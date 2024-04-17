from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.write(f"Score : {self.score}", align="center", font=('Courier', 20))

    def add_one(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=('Courier', 20))