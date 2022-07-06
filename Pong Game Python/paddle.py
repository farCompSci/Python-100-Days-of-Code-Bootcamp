from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_len=1.0,stretch_wid=5)
        self.setposition(position)
        # screen.update()

    def move_up(self):
        y_cor = self.ycor() + 30
        self.sety(y_cor)

    def move_down(self):
        y_cor = self.ycor() - 30
        self.sety(y_cor)