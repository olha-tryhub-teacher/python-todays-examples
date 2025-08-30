# 3. створити 4 об'єкта черепашки - список
turtle_list = []
colors = ["red", "blue", "purple", "orange"]
for col in colors:
    t = create_turtle(randint(-200, 200), -150, col)
    turtle_list.append(t)
