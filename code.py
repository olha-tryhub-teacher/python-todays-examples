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


# 2. Функція - створити об'єкт черепашка(координати та колір). Метод - перетягувати
def create_turtle(x, y, col):
    t = create_t(x, y, "circle", col)

    def on_drag(x, y):
        t.goto(x, y)
        check_turtle()

    t.ondrag(on_drag)
    return t
