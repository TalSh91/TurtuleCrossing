import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
screen.listen()
screen.onkey(player.move_up, "Up")
scoreboard = Scoreboard()
car_manager = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.crate_car()
    car_manager.move_forward()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.finish_line():
        car_manager.lvl_up()
        player.go_to_start()
        scoreboard.lvl_up()



screen.exitonclick()

