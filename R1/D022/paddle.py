from turtle import Turtle

PADDLE_LENGTH = 4

class Paddle(Turtle):
    
    def __init__(self, x_pos):
        self.paddle = []
        self.create_paddle(x_pos)
        
    def create_paddle(self, x_pos):
        for i in range(PADDLE_LENGTH):
            y_pos = 20 * i
            self.add_segment(x_pos, y_pos)
        self.paddle_area = self.paddle_range()
        
    def add_segment(self, x_pos, y_pos):
        paddle_seg = Turtle(shape='square')
        paddle_seg.penup()
        paddle_seg.goto(x_pos, y_pos)
        paddle_seg.color('white')
        self.paddle.append(paddle_seg)
        
    def moveup(self):
        for segment in self.paddle:
            segment.goto(segment.xcor(), segment.ycor() + 20)

    def movedown(self):
        for segment in self.paddle:
            segment.goto(segment.xcor(), segment.ycor() - 20)

    def paddle_range(self):
        return range(self.paddle[0].ycor() - 20, self.paddle[-1].ycor() + 20)