from turtle import *

screen = getscreen()
screen.bgcolor("green")
t = Turtle()


def zone(x, y, count):
    t.clear()
    screen.bgcolor("green")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(75, 360, count)


# ваш код
def draw(x, y):
    if x <= -100:
        zone(-150, 0, 360)
    elif -100 < x <= 100:
        zone(-50, 0, 4)
    elif 100 < x:
        zone(50, 0, 3)


screen.onclick(draw)
