from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.score()

    def score(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
