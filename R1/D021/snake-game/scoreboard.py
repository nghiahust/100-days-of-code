from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.goto(0, 270)
        self.hideturtle()
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   -   High Score: {self.high_score}", align="center", font=("Arial", 8, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
