def click1(x, y):
    t1.lt(randint(30, 200))
    click.count += 1
    click.clear()
    click.write(f"Click: {click.count}", font=("Arial", 24))
