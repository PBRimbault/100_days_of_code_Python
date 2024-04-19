from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Courier'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=(FONT, 20))

    def add_one(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=(FONT, 20))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT, 40))