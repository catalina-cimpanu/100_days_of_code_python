from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("indigo")
        self.setheading(90)
        self.penup()
        self.reset()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

    # def move_right(self):
    #     new_x = self.xcor() + MOVE_DISTANCE
    #     self.goto(new_x, self.ycor())
    #
    # def move_left(self):
    #     new_x = self.xcor() - MOVE_DISTANCE
    #     self.goto(new_x, self.ycor())