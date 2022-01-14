from turtle import Turtle

FONTSIZE = 20

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(position)
        self.write(f"{self.score}", align='center', font=("Arial", FONTSIZE, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align='center', font=("Arial", FONTSIZE, 'normal'))
