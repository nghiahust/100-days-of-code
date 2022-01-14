from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto((-250, 250))
        self.current_lvl = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Level: {self.current_lvl}', align="Center", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.home()
        self.write(f'GAME OVER!', align='Center', font=('Arial', 20, 'normal'))
        self.current_lvl = 1

    def update_score(self):
        self.current_lvl += 1
        self.write_score()
