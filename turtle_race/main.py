from turtle import Turtle, Screen
import random


screen = Screen()
screen_width = int(input("How large do you want the screen to be? "))
screen_height = int(input("How high do you want the screen to be? "))
screen.setup(width=screen_width, height=screen_height)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(title="Make a bet: ", prompt="Which turtle will win the race? Enter a color: ")
is_bet_on = False


turtles = []
i = -screen_height/3
for color in colors:
    new_turtle = Turtle()
    new_turtle.color(color)
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-screen_width/2+10, y=i)
    i += screen_height/7
    turtles.append(new_turtle)

if user_bet:
    is_bet_on = True

winner = ""

while is_bet_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= screen_width/2-25:
            is_bet_on = False
            winner = turtle.pencolor()

if user_bet == winner:
    print(f"{winner.capitalize()} won. You won! Yey!")
else:
    print(f"{winner.capitalize()} won. You lost,maybe next time.")

screen.exitonclick()
