from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() == 0.0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180.0:
            self.segments[0].right(90)
        else:
            print("It cant turn from this position")

    def down(self):

        if self.segments[0].heading() == 0.0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180.0:
            self.segments[0].left(90)
        else:
            print("It cant turn from this position")

    def left(self):
        if self.segments[0].heading() == 90.0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270.0:
            self.segments[0].right(90)
        else:
            print("It cant turn from this position")

    def right(self):
        if self.segments[0].heading() == 90.0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 270.0:
            self.segments[0].left(90)
        else:
            print("It cant turn from this position")

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()