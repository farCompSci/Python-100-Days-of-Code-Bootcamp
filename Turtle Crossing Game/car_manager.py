from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        # self.shape("square")
        self.hideturtle()
        #self.pace = 0.1 # for time.wait

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-240,240)
            new_car.goto(300,rand_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

