# 2. Функція - створити об'єкт черепашка(координати та колір). Метод - перетягувати
def create_turtle(x, y, col):
    t = create_t(x, y, "circle", col)

    def on_drag(x, y):
        t.goto(x, y)
        check_turtle()

    t.ondrag(on_drag)
    return t
