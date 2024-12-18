# # pinky turtle walks in random and changes colour in random

from turtle import Turtle, Screen
import turtle as t
from random import randint, choice

# Initalizing turtle object
pinky = Turtle()
pinky.shape('turtle')
t.colormode(255)

# Generating random number, 0 for left, 1 for right
random_number = randint(0, 1)

# Function for generating random rgb colours.
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0,255)

    color_tuple = (r, g, b)
    return color_tuple

# Navigate motion
random_direction = 200
counter = 0
while random_direction >= counter:
    random_color_selection = random_color()
    random_number = randint(0, 1)
    pinky.color(random_color_selection)
    if random_number == 0:
        pinky.left(90)
        pinky.speed(10)
        pinky.pensize(15)
        pinky.forward(100)
    elif random_number == 1:
        pinky.right(90)
        pinky.speed(4)
        pinky.pensize(15)
        pinky.forward(100)
    counter += 1

screen = Screen()
screen.exitonclick()
