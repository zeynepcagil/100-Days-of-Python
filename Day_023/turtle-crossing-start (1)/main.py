import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move,"w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:
        car_manager.create_car()
    car_manager.move_cars()
    if player.ycor()>265:
        scoreboard.increase_level()
        player.go_to()
        car_manager.clear()
        scoreboard.update_score_board()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:

            scoreboard.game_over()
            game_is_on=False




screen.exitonclick()