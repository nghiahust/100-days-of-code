from turtle import Turtle, Screen
import random
import time

my_turtle = Turtle()
screen = Screen()
screen.clear()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
x_base = -230
y_base = -120


for color in colors:
    my_turtle = Turtle()
    my_turtle.color(color)
    my_turtle.penup()
    my_turtle.shape('turtle')
    my_turtle.goto(x_base, y_base)
    y_base += 50
    turtles.append(my_turtle)
    my_turtle.turtlesize(stretch_wid=2, stretch_len=2, outline=None)


is_on = True
while is_on:
    for turtle in turtles:
        turtle.forward(1)
        if turtle.xcor() >= 200:
            is_on = False
            winner = turtle.pencolor()


if winner.lower() == user_bet.lower():
    print(f"You win the bet. The winner is {winner} turtle.")
else:
    print(f"You lose the bet. The winner is {winner} turtle.")


screen.exitonclick()
