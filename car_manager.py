COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def crate_car(self):
        random_number = random.randint(1,6)
        if random_number == 1:
            new_car = Turtle("square")
            random_y = random.randint(-250,250)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT











