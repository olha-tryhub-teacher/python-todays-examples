# 4. Функція - створити напис-позначку, метод - оновлювати напис
def create_label(x, y):
    t = create_t(x, y, "turtle", "violet")
    t.hideturtle()

    def write_t(count):
        t.clear()
        t.write(f"In rect {count} turtle", font=("Arial", 16))

    t.write_t = write_t
    return t
