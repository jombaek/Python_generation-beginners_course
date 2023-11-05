n = int(input())
digit4 = n % 10
digit3 = n % 100 // 10
digit2 = n % 1000 // 100
digit1 = n // 1000
print('Цифра в позиции тысяч равна', digit1)
print('Цифра в позиции сотен равна', digit2)
print('Цифра в позиции десятков равна', digit3)
print('Цифра в позиции единиц равна', digit4)