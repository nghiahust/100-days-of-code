import colorgram
import turtle as t
import random

#colors = colorgram.extract('image.jpg', 10)
#rgb_colors = []
#for color in colors:
#    rgb = color.rgb
#    red = rgb.r
#    green = rgb.g
#    blue = rgb.b
#    rgb_color = (red, green, blue)
#    rgb_colors.append(rgb_color)
#print(rgb_colors)

color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (222, 231,
237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168,
40), (184, 158, 46)]


my_turtle = t.Turtle()
t.colormode(255)
my_turtle.pensize(20)
my_turtle.penup()
base_x = -200
base_y = -200
my_turtle.setposition(base_x, base_y)
for i in range(10):
    for j in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)
    my_turtle.setposition(base_x, base_y + 50 * (i + 1))


screen = t.Screen()
screen.exitonclick()
