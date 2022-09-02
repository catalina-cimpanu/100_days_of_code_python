from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("misty rose")
        self.goto(0, 260)
        self.score_left = 0
        self.score_right = 0
        self.print_score()

    def increase_score_left(self):
        self.score_left += 1
        self.print_score()

    def increase_score_right(self):
        self.score_right += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.score_left}                                     {self.score_right}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("pink")
        self.write("Game Over", move=False, align="center", font=("Arial", 26, "bold"))