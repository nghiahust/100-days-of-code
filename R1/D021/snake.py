from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)


    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.penup()
        snake.goto(position)
        snake.color('white')
        self.segments.append(snake)


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        
    def prolong(self):
        self.add_segment(self.segments[-1].position())


    def collision_tail(self):
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 10:
                return True
        else:
            return False
