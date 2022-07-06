import random
import time
import turtle
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player_turtle = Player()
car_manager = CarManager()
screen.listen()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    random_chances = random.randint(1,7)
    time.sleep(scoreboard.pace)
    screen.update()
    screen.onkeypress(fun=player_turtle.move_forwards,key="Up")
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if ((player_turtle.distance(car) <= 20) and (car.xcor() <= (player_turtle.xcor() + 20))):
            game_is_on = False
            scoreboard.game_over()
    if player_turtle.ycor() >= 290:
        scoreboard.increase_level()
        player_turtle.goto(player.STARTING_POSITION)
        screen.update()
        time.sleep(0.5)

screen.exitonclick()
