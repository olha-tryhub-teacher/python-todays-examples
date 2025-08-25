# ваш код
from turtle import *
from random import randint


def create_turtle(x, y, sh, col):
    t = Turtle()
    t.pu()
    t.goto(x, y)
    t.width(10)
    t.shape(sh)
    t.color(col)
    return t


# побудувати трасу, де є старт та фініш
def track():
    tr = create_turtle(-150, -150, "triangle", "green")
    tr.pd()
    tr.setheading(90)
    tr.fd(300)
    tr.color("red")
    tr.width(20)
    tr.pu()
    tr.goto(300, -150)
    tr.pd()
    tr.setheading(90)
    tr.fd(300)


# створити черепашок
t1 = create_turtle(-150, 70, "turtle", "purple")
t2 = create_turtle(-150, -70, "turtle", "orange")

track()

# створити ігровий цикл, де черепашки будуть змагатись
while t1.xcor() < 300 and t2.xcor() < 300:
    t1.fd(randint(1, 7))
    t2.fd(randint(1, 7))


if t1.xcor() > t2.xcor():
    t1.write("i am a winner!")
else:
    t2.write("i am a winner!")
