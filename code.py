# 2
while True:
    try:
        players_amount = int(input('Введіть кількість гравців: '))
        bonus_amount = int(input('Введіть кількість бонусів: '))
        break
    except:
        print('Помилка! Кількість повинна бути цілим числом')

# ⬇️⬇️⬇️ Обчислення бонусу з обробкою ділення на 0
try:
    bonus = bonus_amount / players_amount
    print(f"Кожен гравець отримає {bonus} бонусів")
except:
    print("Помилка поділу! Можливо, ніхто не прийшов на турнір?")

# 3
print('Як називається найвища гора світу?')
print('1 - Ельбрус, 2 - Мауна-Лоа, 3 - Еверест, 4 - Деналі')

# тут пиши код ⬇️⬇️⬇️
while True:
    answer = input()
    try:
        answer = int(answer)
        break
    except:
        print("Помилка! Введіть номер правильної відповіді")
# тут пиши код ⬆️⬆️⬆️

if answer == 3:
    print('Абсолютно вірно!')
else:
    print('Ні. Еверест, 8848 метрів')

# 4
print('Як розшифровується ВООЗ?')
print('''1-Всесвітня організація охорони здоров'я''')
print('2-Всеукраїнська організація захисту')
print('3-Всеукраїнська особлива здравниця')
print('4-Володіння особливого значення')

# Допиши програму
while True:
    answer = input()
    try:
        answer = int(answer)
        break
    except:
        print("Помилка! Введіть номер правильної відповіді")

if answer == 1:
    print("Абсолютно вірно!")
else:
    print("Ні. ВООЗ - це Всесвітня організація охорони здоров'я")

# 5
from random import *

random_number = randint(1, 10)

while True:
    answer = input("Вгадай число від 1 до 10:")
    try:
        answer = int(answer)
        if answer < 1 or answer > 10:
            print("Число має бути від 1 до 10.")
        elif answer != random_number:
            print("Спробуй ще раз")
        else:
            print("Вітаю! Ви вгадали!")
            break
    except:
        print("Помилка! Введіть число.")
