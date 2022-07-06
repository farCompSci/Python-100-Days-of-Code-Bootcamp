from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270,270)
        self.level = 1
        self.write(f"Level {self.level}")
        self.pace = 0.1

    def increase_level(self):
        self.pace *= 0.5
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}")

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!",align="center",font=FONT)

