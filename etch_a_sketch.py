from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forward, "f")
screen.onkey(move_backwards, "b")
screen.onkey(right, "r")
screen.onkey(left, "l")
screen.onkey(clear, "c")

screen.exitonclick()
