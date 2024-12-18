# pinky turtle draws a spirograph

from turtle import Turtle, Screen
from random import randint
import turtle as t

pinky = Turtle()
pinky.shape('turtle')
pinky.speed('fastest')
t.colormode(255)

def random_color():
    # Generating random R, G, B
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    # Random color tuple saved to be returned
    random_color_tuple = (r, g, b)

    # Return random number 
    return random_color_tuple

def draw_spirograpgh(size_gap):
    # Make Pinky the turtle to change color and draw circles
    for _ in range(int(360 / size_gap)):
        pinky.color(random_color())
        pinky.circle(100)
        pinky.seth(pinky.heading() + size_gap)

draw_spirograpgh(10)
screen = Screen()
screen.exitonclick()