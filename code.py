from turtle import *
from random import randint

hideturtle()


def create_t(x, y, sh, col):
    t = Turtle()
    t.shape(sh)
    t.speed(0)
    t.color(col)
    t.penup()
    t.goto(x, y)
    return t
