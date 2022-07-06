import time
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Moves the ball"""
        new_ycor = self.ycor() + self.y_move
        new_xcor = self.xcor() + self.x_move
        self.goto(new_xcor,new_ycor)
        # print(f"({self.x_move} , {self.y_move})")

    def bounce_y(self):
        """Bounces ball when it hits top or bottom wall"""
        self.y_move *= -1
        # print(f"({self.x_move} , {self.y_move})")

    def bounce_x(self):
        """Bounces ball when it hits a paddle"""
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed(0.01)
        self.bounce_x()
        self.move()

    # def increase_speed(self):
    #     if self.tempo != 1:
    #         self.tempo -= 1
    #         self.speed(self.tempo)
