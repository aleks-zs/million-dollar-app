import turtle
import colorgram
import random


rgb_colors_bank = []
rgb_bg = ()
colors = colorgram.extract('resources/antipyrylazo.jpg', 20)


def draw_line():
    for x in range(50):
        pointer.dot(9, random.choice(rgb_colors_bank))
        pointer.forward(18)


def set_new_line():
    pointer.setheading(90)
    pointer.forward(18)
    pointer.setheading(180)
    pointer.forward(18 * 50)
    pointer.setheading(0)


def set_initial_position():
    pointer.setheading(218.5)
    pointer.penup()
    pointer.speed('fastest')
    pointer.forward(570)
    pointer.setheading(0)


for c in colors:
    rgb_colors_bank.append((c.rgb.r, c.rgb.g, c.rgb.b))

rgb_bg = rgb_colors_bank[0]
rgb_colors_bank.pop(0)

screen = turtle.Screen()
screen.setup(920, 755)
turtle.colormode(255)
screen.bgcolor(rgb_bg)
pointer = turtle.Turtle()

set_initial_position()
for counter in range(41):
    draw_line()
    set_new_line()

pointer.hideturtle()
screen.exitonclick()
