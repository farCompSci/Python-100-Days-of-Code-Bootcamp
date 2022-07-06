from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        # self.high_score = content
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score: {self.score} , High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} , High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",font=FONT,align=ALIGNMENT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as new_data:
                new_data.write(str(self.score))
            self.high_score = self.score
        self.clear()
        self.score = 0
        self.write(f"Score: {self.score} , High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

