
print('Ласкаво просимо!', student_card)

while True:
    answer = int(input('Особистий кабінет: 1 - взяти, 2 - повернути, 3 - додому'))

    if answer == 1:
        title = input('Введіть назву:')
        student_card['борг'] = title
    elif answer == 2:
        if 'борг' in student_card:
            del student_card['борг']
    elif answer == 3:
        break

    print('Картка читача:', student_card)
print('Чекаємо на вас:', student_card)
