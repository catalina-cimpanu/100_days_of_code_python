from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("midnight blue")
        self.goto(-200, 260)
        self.level = 0
        self.level_speed = 0.1
        self.print_score()

    def increase_level(self):
        self.level += 1
        self.level_speed *= 0.9
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("midnight blue")
        self.write("Game Over", move=False, align="center", font=("Arial", 26, "bold"))