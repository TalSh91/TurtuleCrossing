FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.lvl = 1
        self.goto(-210, 260)
        self.update_lvl_up()


    def update_lvl_up(self):
        self.clear()
        self.write(f"Level: {self.lvl}", align="center", font=(FONT))

    def lvl_up(self):
        self.lvl += 1
        self.update_lvl_up()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=(FONT))




