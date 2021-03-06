from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.setheading(90)
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if self.ycor() < FINISH_LINE_Y:
            self.goto(self.xcor(), new_y)

    def restart(self):
        self.clear()
        self.goto(STARTING_POSITION)
