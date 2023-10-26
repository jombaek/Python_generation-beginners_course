num = int(input())
min_digit, max_digit = 9, 0

while num:
    digit = num % 10
    
    max_digit = max(digit, max_digit)
    min_digit = min(digit, min_digit)

    num //= 10

print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)