
# 5. Створити напис-позначку
label = create_label(-150, -125)


# 6.Функція - перевірити кількість черпашок у прямокутнику
def check_turtle():
    count = 0
    for t in turtle_list:
        if abs(t.xcor()) < 150 and abs(t.ycor()) < 100:
            count += 1

    label.write_t(count)


# 7. Намалювати ігрове поле, перевірити де черепашки піся спавну
draw_field()
check_turtle()
