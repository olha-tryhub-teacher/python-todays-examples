# 4. Ігровий цикл
while click.count < 20 and runner.count < 4:
    if abs(t1.xcor()) < 200 and abs(t1.ycor()) < 200:
        t1.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))


# 5. Переврка виграшу/програшу
if click.count >= 20:
    click.pu()
    click.goto(0, 0)
    click.write("You winn", font=("Arial", 40))
# те саме тільки раннер
if runner.count >= 4:
    runner.pu()
    runner.goto(0, 0)
    runner.write("You lose", font=("Arial", 40))
