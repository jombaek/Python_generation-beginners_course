n = int(input())
digit3 = n % 10
digit2 = n // 10 % 10
digit1 = n // 100
print('Сумма цифр =', digit1 + digit2 + digit3)
print('Произведение цифр =', digit1 * digit2 * digit3)