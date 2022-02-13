from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_right():
    angle_increase = 10
    current_heading = tim.heading()
    new_heading = current_heading - angle_increase
    tim.setheading(new_heading)

def rotate_left():
    angle_increase = 10
    current_heading = tim.heading()
    new_heading = current_heading + angle_increase
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=rotate_left, key='a')
screen.onkey(fun=rotate_right, key='d')
screen.onkey(fun=clear, key='c')

screen.exitonclick()