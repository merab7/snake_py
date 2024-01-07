from turtle import Turtle
import random


class Food:
    def __init__(self):
        self.s = Turtle()
        self.score = []
        self.xcor = random.randint(-280, 280)
        self.ycor = random.randint(-280, 280)
        self.create_dot()

    def create_dot(self):
        self.s.dot(20, "blue")
        self.s.hideturtle()

    def goto(self):
        self.s.clear()
        self.s.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.create_dot()
