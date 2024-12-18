# pinky turtle draws a shape from triangle to decagon

from turtle import Turtle, Screen

pinky = Turtle()

pinky.shape('turtle')

def draw_triangle():
    for _ in range(3):
        pinky.forward(100)
        pinky.right(120)

def draw_square():
    for _ in range(4):
        pinky.forward(100)
        pinky.right(90)

def draw_pentagon():
    for _ in range(5):
        pinky.forward(100)
        pinky.right(72)

def draw_hexagon():
    for _ in range(6):
        pinky.forward(100)
        pinky.right(60)

def draw_septagon():
    for _ in range(7):
        pinky.forward(100)
        pinky.right(51.43)

def draw_octagon():
    for _ in range(8):
        pinky.forward(100)
        pinky.right(45)

def draw_nonagon():
    for _ in range(9):
        pinky.forward(100)
        pinky.right(40)

def draw_decagon():
    for _ in range(10):
        pinky.forward(100)
        pinky.right(36)


draw_triangle()
draw_square()
draw_pentagon()
draw_hexagon()
draw_septagon()
draw_octagon()
draw_nonagon()
draw_decagon()


screen = Screen()
screen.exitonclick()