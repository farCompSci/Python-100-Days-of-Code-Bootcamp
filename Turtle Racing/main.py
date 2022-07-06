import random
import turtle
from turtle import Turtle,Screen

# tim = Turtle("turtle") # you can specify the shape in the constructor
# tim.penup()
# is_bet_on = False
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title ="Make your bet", prompt = "Which turtle will win the race? Enter a color: ").lower()
print(user_bet)
turtles = []
colors = ["red","orange","yellow","green","blue","violet"]
y_pos = [-120,-70,-20,30,80,120]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    turtles.append(new_turtle)
    new_turtle.goto(x=-230,y=y_pos[turtle_index])

is_bet_on = True
while is_bet_on:
    for animal in turtles:
        random_distance = random.randint(0,10)
        animal.forward(random_distance)
        if animal.xcor() >= 230:
            winner = animal
            is_bet_on = False
if user_bet == winner:
    print(f"You won, {winner.pencolor()} was first")
else:
    print(f"You lost, {winner.pencolor()} was first")

# for _ in range(len(colors)):
#     new_turtle = Turtle("turtle")
#     new_turtle.penup()
#     new_turtle.color(colors[_])
#     new_turtle.setposition(x=-239,y=y_pos)
#     turtles.append(new_turtle)
#     y_pos += 50
# # print(turtles)
#
# continue_playing = True
# while continue_playing:
#     chosen_turtle = random.choice(turtles)
#     chosen_turtle.forward(random.randint(5,10))
#     for element in turtles:
#         if element.xcor() >= 250:
#             print(f"{element.color()} won this race")
#             winner = element.color()
#             continue_playing = False
# if user_bet == winner:
#     print("You won!")
# else:
#     print(f"You lost, {winner} won")
screen.exitonclick()