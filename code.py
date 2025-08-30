# 1.Функція - малюємо ігрове поле
def draw_field():
    t = create_t(-150, -100, "turtle", "gold")
    t.hideturtle()
    t.width(10)
    t.pendown()
    for _ in range(2):
        t.fd(300)
        t.lt(90)
        t.fd(200)
        t.lt(90)
