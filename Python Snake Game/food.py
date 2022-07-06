from turtle import Turtle
import random

class Food(Turtle): # putting turtle as superclass

    def __init__(self):
        super().__init__() #use super instead of actual name of class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) # this scales the size of the circle to 10, as it starts at 20
        self.color("yellow")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
