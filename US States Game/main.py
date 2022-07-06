# How to get x and y values from clicking on the map
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()

# answer_state = screen.textinput(title="Guess the State",prompt="What's another State's name?")
# screen.exitonclick()

########################################################################################################################

                                    # Guess The State Game Code Below #

########################################################################################################################


#TODO 1: Using Pandas, find a way to get a hold of the coordinates of the states
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")

#Create a new turtle shape, in this case make the image a turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Store State Names and Coordinates from csv file into data
data = pandas.read_csv("50_states.csv")

game_is_on = True
score = 0
guessed = []
while game_is_on:
    user_guess = screen.textinput(title=f"Score: {score}/50", prompt="Guess a state")

    if user_guess == "Exit":
        break

    # guessed = [state for state in data.state if element.lower() == user_guess]
    for state in data.state:
        """Writes the name of the state at the state's coordinates if the user guesses right"""
        if user_guess.lower() == state.lower():
            new_turtle = turtle.Turtle()
            new_turtle.hideturtle()
            new_turtle.penup()
            """Getting the coordinates in int form and setting them as the turtle's coordinates"""
            new_turtle.goto(int(data[data.state == state].x),int(data[data.state == state].y))
            new_turtle.write(f"{state}")
            guessed.append(state)
            recurrence = 0

            for element in guessed:
                """Counts the occurrences of the element in the guesses, if it was already there do not add a point, else do"""
                if state == element:
                    recurrence += 1
            if recurrence < 2:
                """Add a point if it's a new guess"""
                score += 1

# not_guessed = []
if score != 50:
    not_guessed = [state for state in data.state if state not in guessed]

not_guessed_states = pandas.DataFrame(not_guessed)
not_guessed_states.to_csv("not_guessed_states.csv")


screen.exitonclick()


