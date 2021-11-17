from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score {self.current_score}", align="center", font=FONT)
        self.hideturtle()

    def refresh(self):
        self.write(f"Score {self.current_score}", align="center", font=FONT)

    def increase(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score {self.current_score}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

