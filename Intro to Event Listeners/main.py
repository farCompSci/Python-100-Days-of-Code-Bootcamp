import turtle
from turtle import Screen,Turtle

tim = Turtle()
tim.speed("fastest")
screen = Screen()
screen.listen()
starting_angle = 0
def mv_fw():
    tim.forward(10)
def mv_bk():
    tim.backward(10)
def mv_rt():
    #tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def mv_lt():
    #tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clr_scr():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkeypress(mv_fw,"w")
screen.onkeypress(mv_bk,"s")
screen.onkeypress(mv_rt,"d")
screen.onkeypress(mv_lt,"a")
screen.onkeypress(clr_scr,"c")

#make the parameter of the function the keystroke



screen.exitonclick()

