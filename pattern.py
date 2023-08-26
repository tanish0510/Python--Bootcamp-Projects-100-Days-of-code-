import turtle
from turtle import Turtle
import random

turtle.colormode(255)
timmy = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")
for _ in range(345):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

