import turtle as t
import random


circle_number = 50
angle = 360 / circle_number
my_turtle = t.Turtle()
t.colormode(255)
base_angle = 0
my_turtle.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for _ in range(circle_number):
    my_turtle.color(random_color())
    my_turtle.circle(100,None,None)
    base_angle += angle
    my_turtle.setheading(base_angle)



screen = t.Screen()
screen.exitonclick()
