from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)  # use keyword argument to make it clearer
screen.bgcolor("black")
screen.title("My Snake Game")  # can change
screen.tracer(0)
"""Turns of the tracer, because the drawing and updates are not shown . Screen does not refresh unless updates"""

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # score.game_over()
        score.reset()
        snake.reset()
        # game_is_on = False

    # detect collision with tail
    for segment in snake.segments[1:]: # using slicing, this loops through every segment in the array without looking at position 0
        if snake.head.distance(segment) < 10:
            # score.game_over()
            score.reset()
            snake.reset()
            # game_is_on = False

# def turtle_creator(blk_count):
#   """Turtle maker function"""
#     new_turtle = Turtle("square")
#     new_turtle.penup()
#     new_turtle.color("white")
#     new_turtle.goto(x=-20*blk_count,y=0)
#     blk_count += 1
#
# turtle_creator(1)
# turtle_creator(2)
# turtle_creator(3)

screen.exitonclick()
