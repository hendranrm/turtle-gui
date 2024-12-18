# pinky turtle draws a heart

from turtle import Turtle, Screen

pinky = Turtle()
pinky.pencolor("red")

def curve(): 
    for i in range(200): 
        # Defining step by step curve motion 
        pinky.right(1) 
        pinky.forward(1) 

def draw_heart():
    pinky.color('red')
    pinky.begin_fill()
    pinky.left(140)
    pinky.forward(113)
    curve()
    pinky.left(120)
    curve()
    pinky.forward(112)
    pinky.end_fill()
    

draw_heart()
screen = Screen()
screen.exitonclick()