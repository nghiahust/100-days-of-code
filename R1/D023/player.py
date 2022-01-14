from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self, starting_pos):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.starting_pos = starting_pos
        self.goto(self.starting_pos)
        self.color('black')

    def go_up(self):
        if self.ycor() < 250:
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -250:
            self.forward(-MOVE_DISTANCE)

    def go_left(self):
        if self.xcor() > -250:
            new_xcor = self.xcor() - MOVE_DISTANCE
            self.setx(new_xcor)

    def go_right(self):
        if self.xcor() < 250:
            new_xcor = self.xcor() + MOVE_DISTANCE
            self.setx(new_xcor)

    def reset_position(self):
        self.goto(self.starting_pos)
