from turtle import *

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

# t1.speed(10)
# t2.speed(10)
# t3.speed(10)

t2.right(120)
t3.left(120)

t1.color("blue")
t2.color("red")
t3.color("green")


c = 0
while c < 9:
    t1.forward(50)
    t1.left(40)
    t2.forward(50)
    t2.left(40)
    t3.forward(50)
    t3.left(40)
    c += 1
