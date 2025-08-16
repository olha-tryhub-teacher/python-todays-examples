# 2.Лейбли-лічильник
click = create_t(200, 100, 0, "blue")
click.count = 0
click.ht()
click.write(f"Click: {click.count}", font=("Arial", 24))

# те саме тільки раннер
runner = create_t(200, 150, 0, "red")
runner.count = 0
runner.ht()
runner.write(f"Runner: {runner.count}", font=("Arial", 24))
