import turtle
from turtle import Turtle, Screen
import random


def random_color():
    turtle.colormode(255)
    turtle.bgcolor("black")
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_polygon_spirograph(gap_size, sides):
    tim.hideturtle()
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        for _ in range(sides):
            tim.fd(100)
            tim.rt(int(360 / sides))
        tim.left(gap_size)


def draw_circle_spirograph(gap_size):
    tim.hideturtle()
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(300)
        tim.left(gap_size)


tim = Turtle()
tim.speed(0)

for num_sides in range(3, 11):
    draw_polygon_spirograph(5, num_sides)
    tim.clear()

draw_circle_spirograph(5)

screen = Screen()
screen.exitonclick()
