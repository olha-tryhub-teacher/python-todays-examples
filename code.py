# 4. Ігровий цикл
while click.count < 20 and runner.count < 4:
    if abs(t1.xcor()) < 200 and abs(t1.ycor()) < 200:
        t1.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))

    if abs(t2.xcor()) < 200 and abs(t2.ycor()) < 200:
        t2.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))

    if abs(t3.xcor()) < 200 and abs(t3.ycor()) < 200:
        t3.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))

    if abs(t4.xcor()) < 200 and abs(t4.ycor()) < 200:
        t4.fd(2)
    else:
        runner.count += 1
        runner.clear()
        runner.write(f"Runner: {runner.count}", font=("Arial", 24))
    sleep(0.1)

# 5. Переврка виграшу/програшу
if click.count >= 20:
    click.pu()
    click.goto(0, 0)
    click.write("You winn", font=("Arial", 40))
if runner.count >= 4:
    runner.pu()
    runner.goto(0, 0)
    runner.write("You lose", font=("Arial", 40))
