col1 = input()
col2 = input()

if col1 == 'красный':
    if col2 == 'красный':
        print('красный')
    elif col2 == 'синий':
        print('фиолетовый')
    elif col2 == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif col1 == 'синий':
    if col2 == 'красный':
        print('фиолетовый')
    elif col2 == 'синий':
        print('синий')
    elif col2 == 'желтый':
        print('зеленый')
    else:
        print('ошибка цвета')
elif col1 == 'желтый':
    if col2 == 'красный':
        print('оранжевый')
    elif col2 == 'синий':
        print('зеленый')
    elif col2 == 'желтый':
        print('желтый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')