import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
manager = CarManager()
player1 = Player()
screen.listen()
screen.onkey(player1.move_up, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.make_car()
    manager.move_cars()
    if player1.ycor() >= 280:
        player1.restart()
        scoreboard.refresh()
        scoreboard.increase()
        manager.level_up()
    for car in manager.cars:
        if player1.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
