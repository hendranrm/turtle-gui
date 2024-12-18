# pinky turltle extracts colour based on a jpeg

import colorgram
from turtle import Turtle, Screen
import turtle as t
from random import choice

#Extract colours
colours = colorgram.extract('hirst_painting/hirst_spot_painting.jpg', 7)
t.colormode(255)

rgb_colours = []
for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)

    rgb_colours.append(new_color)

color_list = rgb_colours.copy()


tim = Turtle()
tim.shape('turtle')

tim.penup()


tim.setx(-200)
tim.sety(-200)
update_x_coordinate = -200
update_y_coordinate = -200

for row in range(10):
    x_coordinate = update_x_coordinate 
    y_coordinate = update_y_coordinate
    tim_coordinate = (x_coordinate, y_coordinate)
    tim.setx(tim_coordinate[0])
    tim.sety(tim_coordinate[1])
    update_y_coordinate += 30

    for number in range(10):
        color = choice(color_list)
        tim.dot(20,color)
        tim.fd(50)

screen = Screen()
screen.exitonclick()

