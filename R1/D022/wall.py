from turtle import Turtle

WALL_SIZE = 10

class Wall(Turtle):
    
    def __init__(self, y_pos, length):
        self.wall = []
        self.create_wall(length, y_pos)
        
    def create_wall(self, length, y_pos):
        i = 0
        while i <= length / 2:
            self.add_segment(i, y_pos)
            self.add_segment(-i, y_pos)
            i += WALL_SIZE
        
    def add_segment(self, x_pos, y_pos):
        segment = Turtle(shape='square')
        segment.shapesize(0.5, 0.5)
        segment.penup()
        segment.goto(x_pos, y_pos)
        segment.color('white')
        self.wall.append(segment)
        
class MiddleWall(Turtle):

    def __init__(self, length):
        self.wall = []
        self.create_wall(length)
        
    def create_wall(self, length):
        i = 0
        while i <= length / 2:
            self.add_segment(0, i)
            self.add_segment(0, -i)
            i += WALL_SIZE*2
        
    def add_segment(self, x_pos, y_pos):
        segment = Turtle(shape='square')
        segment.shapesize(0.5, 0.1)
        segment.penup()
        segment.goto(x_pos, y_pos)
        segment.color('white')
        self.wall.append(segment)
