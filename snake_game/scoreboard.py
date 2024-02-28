from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score=0
        self.color("white")
        self.penup()
        self.update()
        self.hideturtle()
        self.goto(0, 270)

    # def game_over(self):
    #     self.write("Game Over", align="center", font=('Arial', 24, 'normal'))
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score=0
        self.update()
    def increase(self):
        self.score += 1

        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score={self.high_score}", align="center", font=('Arial', 24, ' normal'))
