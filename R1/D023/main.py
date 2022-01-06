from turtle import Screen
from player import Player
from car_management import Cars
from scoreboard import ScoreBoard
import time


# Create the screen
screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.title('Turtle Cross Street')
screen.tracer(0)

# Player
player = Player((0, -250))
screen.listen()
screen.onkey(fun=player.go_up, key='Up')
screen.onkey(fun=player.go_down, key='Down')
screen.onkey(fun=player.go_left, key='Left')
screen.onkey(fun=player.go_right, key='Right')

# Car management
cars = Cars()

# Scoreboard
score = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)
    cars.car_move()
    for car in cars.cars:
        if car.xcor() - 30 < player.xcor() < car.xcor() + 30 and car.ycor() - 25 < player.ycor() < car.ycor() + 20:
            score.game_over()
            game_on = False

    if player.ycor() >= 250:
        player.reset_position()
        cars.speed_up()
        score.update_score()


screen.exitonclick()
