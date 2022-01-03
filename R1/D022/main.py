from turtle import Screen
from paddle import Paddle
from pong import Pong
from wall import Wall, MiddleWall
from score import Score
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

player1 = Paddle(0 - SCREEN_WIDTH / 2 + 20)
score1 = Score((-50, SCREEN_HEIGHT / 2 - 50))
player2 = Paddle(SCREEN_WIDTH / 2 - 20)
score2 = Score((50, SCREEN_HEIGHT / 2 - 50))


pong = Pong()

upper_wall = Wall(SCREEN_HEIGHT / 2, SCREEN_WIDTH)
lower_wall  = Wall(-SCREEN_HEIGHT / 2, SCREEN_WIDTH)
middle_wall = MiddleWall(SCREEN_HEIGHT)

screen.listen()
screen.onkey(player1.moveup,"w")
screen.onkey(player1.movedown, "s")
screen.onkey(player2.moveup, "i")
screen.onkey(player2.movedown, "k")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.001)
    pong.move()

    #Bouncing logic
    if pong.pong.ycor() >= (SCREEN_HEIGHT / 2 - 15) or pong.pong.ycor() <= (-SCREEN_HEIGHT / 2 + 15):
        pong.bounce_wall()
    if pong.pong.xcor() >= (SCREEN_WIDTH / 2 - 40) and int(pong.pong.ycor()) in player2.paddle_range():
        pong.bounce_paddle()
    if pong.pong.xcor() <= (-SCREEN_WIDTH / 2 + 40) and int(pong.pong.ycor()) in player1.paddle_range():
        pong.bounce_paddle()

    #Scoring
    if pong.pong.xcor() > (SCREEN_WIDTH / 2):
        score1.increase_score()
        pong.reset_pong()
    if pong.pong.xcor() < (-SCREEN_WIDTH / 2):
        score2.increase_score()
        pong.reset_pong()


screen.exitonclick()
