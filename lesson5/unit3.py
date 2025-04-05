# 1
print("🚴 Велосипедист починає свій шлях від старту до фінішу! 🚴")
finish = ""
dist = int(input("Довжина траси:"))
velo = "🏁" + dist * "➖" + "🚴" + "🏁"
velo += "\n"
back = 0
while dist > 0:
    move = int(input("Скільки проїхав?"))
    if dist - move >= 0:
        back += move
        dist = dist - move
        row = dist * "➖" + "🚴" + back * "➖"
        velo += "🏁" + row + "🏁" + "\n"
    else:
        print("Неможливо! Перепитай художника!")
print(velo)

print("Велосипедист 🚴 успішно доїхав до фінішу! 🏁")

# 2
print("Художник малює нічне небо 🌌 зі зірками та місяцем 🌙!")
width = int(input("Введіть ширину полотна: "))
height = int(input("Введіть висоту полотна: "))
stars = int(input("Введіть кількість зірок?"))
while (width * height - 1) < stars:
    print("Така кількість зірок не вміститься на картині!")
    stars = int(input("Введіть кількість зірок?"))

count = 1
for y in range(height):
    row = ""
    for x in range(width):
        if y == 0 and x == (width - 1):
            row += "🌙"
            continue
        if count % 3 == 0 and stars > 0:
            row += "⭐️"
            stars -= 1
        else:
            row += "🌌"
        count += 1

    print(row)

# 3
print("Художник малює поле з квітами 🌹🌷🌼!")
t = int(input("троянд:"))
tt = int(input("тюльпанів:"))
r = int(input(" ромашек:"))
while (t + tt + r) % 6 != 0:
    print("Загальна кількість не кратна 6!")
    t = int(input("троянд:"))
    tt = int(input("тюльпанів:"))
    r = int(input(" ромашек:"))

pole = ""
count = 0
while (t + tt + r) > 0:
    if t > 0:
        pole += "🌹"
        t -= 1
        count += 1
    if tt > 0:
        pole += "🌷"
        tt -= 1
        count += 1
    if r > 0:
        pole += "🌼"
        r -= 1
        count += 1
    if count == 6:
        pole += "\n"
        count = 0

print(pole)
