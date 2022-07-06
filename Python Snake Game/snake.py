import time
from turtle import Turtle, Screen, heading, setheading

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # starting_positions
    # segments = []

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # self.starting_positions = [(0, 0), (-20, 0), (-40, 0)] Instructor put it as a constant

    def create_snake(self):
        for position in STARTING_POSITIONS:
            """Creates new turtle objects and appends them to the segment array"""
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Appends an element to the segment array, it appears that the index number does not matter as long as it exists because we use the append function"""
        self.add_segment(self.segments[-1].position()) # gets a hold of the last segment in the array, using the index -1

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0,
                             -1):  ### loops from the last element to the 0th element in the list, with steps of -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            """This makes sure that the last segment moves to the place of the previous one in order of list indices
                   If we move the head, the second piece will move where the head was, the third piece will move to where the second was, etc
                   This makes sure that they will all move more or less as a block given how the screen refreshes"""
        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].setheading(0)

    def up(self):
        if self.head.heading != (DOWN):
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]