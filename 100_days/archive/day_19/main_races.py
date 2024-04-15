from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue"]
y_space = 40
y_count = -2
all_turtles = []

for turtle in colors: 
    y_value = y_count * y_space
    y_count += 1
    color = turtle   
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(screen.window_width()/(-2) + 20, y_value)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > screen.window_width()/(2) - 20:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()