from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(300, random.randint(-250, 250))

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())