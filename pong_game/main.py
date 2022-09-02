from turtle import Turtle, Screen
import time
from board import ScoreBoard
from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.bgcolor("dark slate gray")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("PONG")
screen.tracer(0)

score_board = ScoreBoard()

paddle_1 = Paddle()
paddle_1.player_right()
paddle_2 = Paddle()
paddle_2.player_left()

ball = Ball()

screen.listen()
screen.onkeypress(paddle_1.move_up, "Up")
screen.onkeypress(paddle_1.move_down, "Down")
screen.onkeypress(paddle_2.move_up, "w")
screen.onkeypress(paddle_2.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if paddle_1.distance(ball) < 50 and ball.xcor() > 325:
        ball.bounce_x()
        ball.increase_speed()

    # Detect collision with left paddle
    if paddle_2.distance(ball) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        ball.increase_speed()

    # Detect if ball not caught
    # right
    if ball.xcor() > 380:
        score_board.increase_score_left()
        ball.reset()
    # left
    elif ball.xcor() < -380:
        score_board.increase_score_right()
        ball.reset()

screen.exitonclick()
