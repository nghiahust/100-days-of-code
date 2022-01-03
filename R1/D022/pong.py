from turtle import Turtle
import random

PONG_DIRECTION = (45, 135, 225, 315)
BOUNCE_WALL_DIRECTION = {45: 315, 135: 225, 225: 135, 315: 45}
BOUNCE_PADDLE_DIRECTION = {45: 135, 135: 45, 225: 315, 315: 225}
BOUNCING = {
    "upper_wall": {45: 315, 135: 225},
    "lower_wall": {225: 135, 315: 45},
    "right_paddle": {45: 135, 315: 225},
    "left_paddle": {135: 45, 225: 315}
}

class Pong(Turtle):

    def __init__(self):
        self.create_pong()

    def create_pong(self):
        self.pong = Turtle(shape='circle')
        self.pong.penup()
        self.pong.color('white')
        self.pong.setheading(random.choice(PONG_DIRECTION))

    def move(self):
        self.pong.forward(1)

    def bounce(self, target):
        self.pong.setheading(BOUNCING[target][self.pong.heading()])

    def bounce_wall(self):
        if self.pong.ycor() > 0:
            self.bounce('upper_wall')
        else:
            self.bounce('lower_wall')

    def bounce_paddle(self):
        if self.pong.xcor() > 0:
            self.bounce('right_paddle')
        else:
            self.bounce('left_paddle')

    def reset_pong(self):
        self.pong.home()
        self.pong.setheading(random.choice(PONG_DIRECTION))
