from turtle import Screen,Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

score = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
# ball.left(37)

score_r = 0
score_l = 0
continue_game = True
while continue_game:
    time.sleep(ball.move_speed)
    screen.onkeypress(fun=r_paddle.move_up,key="Up")
    screen.onkeypress(fun=r_paddle.move_down,key="Down")
    screen.onkeypress(fun=l_paddle.move_up,key="w")
    screen.onkeypress(fun=l_paddle.move_down,key="s")

    ball.move()
    #detect collision

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #detect collision with paddle
    if (r_paddle.distance(ball) <= 55 and ball.xcor() > 320) or (l_paddle.distance(ball) <= 55 and ball.xcor() < -320):
        # print("Made contact")
        ball.bounce_x()
        ball.move_speed *= 0.9
        # ball.increase_speed()

    #detect if points are scored
    if ball.xcor() >= 390:
        score.l_point()
        ball.reset_position()
        screen.update()
        time.sleep(2)
        
    elif ball.xcor() <= -390:
        score.r_point()
        ball.reset_position()
        screen.update()
        time.sleep(2)



    screen.update()


screen.exitonclick()
