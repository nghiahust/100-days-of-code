from turtle import Turtle
import random

COLORS = (
'blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive',
'cyan')
SCREEN_LIMIT = -350
MAX_CARS = 20


class Cars(Turtle):

    def __init__(self):
        self.car = None
        self.cars = []
        self.speed = 1
        for _ in range(MAX_CARS):
            self.create_car()

    def create_car(self):
        self.car = Turtle()
        self.car.penup()
        self.car.shape('square')
        self.car.shapesize(stretch_len=2, stretch_wid=1)
        self.car.color(random.choice(COLORS))
        self.car.goto(random.choice(range(300, 1000, 50)),
                      random.choice(range(-200, 200, 25)))
        self.car.setheading(180)
        self.cars.append(self.car)

    def car_move(self):
        for car in self.cars:
            if car.xcor() < SCREEN_LIMIT:
                car.color(random.choice(COLORS))
                car.goto(random.randint(300, 1000), random.randint(-250, 250))
            car.forward(self.speed)

    def speed_up(self):
        self.speed *= 1.1
