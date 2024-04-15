# from turtle import Turtle, Screen

# from random import randint, random


# tim = Turtle()

# tim.shape("turtle")
# tim.speed(0)


# def random_walk():

#     angle = 90 * randint(0, 3)
#     tim.pencolor((random(), random(), random()))

#     tim.setheading(angle)

#     tim.forward(20)


# def draw_spirograph(steps, radius):

#     iteration_angle = 360 / steps

#     heading = 0

#     for step in range(steps):

#         heading += iteration_angle 
#         tim.pencolor((random(), random(), random()))

#         tim.setheading(heading)

#         tim.circle(radius)


# draw_spirograph(100, 100)


# # for step in range(500):

# #     random_walk()


# screen = Screen()


# screen.exitonclick()

# import colorgram


# # Extract 6 colors from an image

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
from random import randint, random, choice

color_list = [(220, 153, 106), (132, 171, 196), (221, 72, 88), (216, 131, 149), (23, 119, 153), (242, 208, 98), (120, 176, 148), (37, 119, 82), (20, 164, 204), (141, 86, 62), (221, 82, 76), (125, 86, 105), (174, 184, 216), (20, 167, 121), (162, 209, 167), (3, 97, 117), (175, 155, 74), (55, 60, 94), (236, 162, 174), (240, 167, 154), (147, 207, 222), (22, 100, 84), (48, 63, 75), (97, 119, 172)]

tim = turtle_module.Turtle()

tim.shape("turtle")
tim.speed(0)
tim.penup()
tim.hideturtle()

turtle_module.colormode(255)

for y in range(-5, 5):
    tim.sety(50 * y)
    for x in range(-5, 5):
        tim.setx(50 * x)
        tim.dot(20, (choice(color_list)))

screen = turtle_module.Screen()
screen.exitonclick()