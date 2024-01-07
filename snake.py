from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        s = Turtle()
        s.speed("fastest")
        s.shape("square")
        s.color("white")
        s.penup()
        s.goto(position)
        self.segments.append(s)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[num - 1].xcor()
            new_y_cor = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x_cor, new_y_cor)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def self_crush(self):
        for x in self.segments:
            if x != self.head:
                if self.head.distance(x) < 10:
                    return True
