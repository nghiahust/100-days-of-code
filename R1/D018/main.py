from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("aqua")


for i in range(3, 10):
    colour = (random.choice(range(255)), random.choice(range(255)), random.choice(range(255)))
    my_turtle.color(colour)
    num_sides = i
    angle = 360 / num_sides
    # my_turtle.speed(0)
    for _ in range(num_sides):
        my_turtle.forward(50)
        my_turtle.right(angle)