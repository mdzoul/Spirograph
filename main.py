# Basic Circle Spirograph
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


def draw_spirograph(gap_size):
    tim.hideturtle()
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(gap_size)


tim = Turtle()
tim.speed(0)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
