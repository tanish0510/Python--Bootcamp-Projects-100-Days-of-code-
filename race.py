from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1000, height=1000)
screen.setup(width=1000, height=1000)
user_bet = screen.textinput(title="Place your bet", prompt="Which Turtle will win ? Enter your color:")
color = ["red", "yellow", "blue", "green", "purple", "orange", "white"]
y_pos = [-300, -200, -100, 0, 100, 200, 300]
all_turtles = []
for turtle_index in range(0, 7):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(color[turtle_index])
    timmy.goto(x=-450, y=y_pos[turtle_index])
    all_turtles.append(timmy)

if user_bet:
    race_on = True
while race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 470:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won your {winning_color} turtle has won")
            else:
                print(f"You lose your {user_bet} turtle has lost ,{winning_color} won")
        distance = random.randint(0, 20)
        turtle.forward(distance)
screen.exitonclick()
