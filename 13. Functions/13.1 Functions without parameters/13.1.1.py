# объявление функции
def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            sep = '*'
        else:
            sep = ' '

        print('*', '*', sep=sep * 8)

# основная программа
draw_box()  # вызов функции
