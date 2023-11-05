n = int(input())
digit4 = n % 10
digit3 = n % 100 // 10
digit2 = n % 1000 // 100
digit1 = n // 1000

if digit1 + digit4 == digit2 - digit3:
    print('ДА')
else:
    print('НЕТ')