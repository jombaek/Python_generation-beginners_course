# объявление функции
def draw_triangle(fill, base):
    for i in range(base):
        for j in range(i + 1):
            if i + j >= base:
                break
            print(fill, end='')
        print()

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)