from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in POSITIONS:
            s = Turtle()
            s.shape("square")
            s.color("white")
            s.penup()
            s.goto(pos)
            self.segments.append(s)

    def move(self):
        for seg in self.segments:
            if seg == self.segments[-1]:
                seg.forward(SPEED)
            else:
                seg.goto(self.segments[self.segments.index(seg) + 1].pos()[0],
                         self.segments[self.segments.index(seg) + 1].pos()[1])

    def up(self):
        if self.segments[-1].heading() != 270:
            self.segments[-1].setheading(90)

    def down(self):
        if self.segments[-1].heading() != 90snakedays:
            self.segments[-1].setheading(270)

    def right(self):
        if self.segments[-1].heading() != 180:
            self.segments[-1].setheading(0)

    def left(self):
        if self.segments[-1].heading() != 0:
            self.segments[-1].setheading(180)
