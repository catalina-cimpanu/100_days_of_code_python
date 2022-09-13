import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white smoke")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")
# screen.onkeypress(player.move_right, "Right")
# screen.onkeypress(player.move_left, "Left")

cars = []
loop = 0

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.level_speed)
    screen.update()
    for car in cars:
        car.move()
        # Detect collision with car
        if car.distance(player) <= 15:
            game_is_on = False
            scoreboard.game_over()

    # Detect getting to finish line
    if player.ycor() >= 280:
        scoreboard.increase_level()
        player.reset()

    loop += 1
    if loop % 10 == 0:
        car = CarManager()
        cars.append(car)

screen.exitonclick()
# note for myself: i solved this by myself and although the code is rather messy in comparison with what she did,
# i prefer to keep it like this, cuz it's functioning
