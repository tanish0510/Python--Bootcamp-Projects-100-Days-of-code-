from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.update()
        self.hideturtle()
        self.goto(0, 270)

    def game_over(self):
        self.write("Game Over", align="center", font=('Arial', 24, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, ' normal'))
