num = int(input())
has_same_digits = True
last_digit = num % 10

while num:
    digit = num % 10

    if last_digit != digit:
        has_same_digits = False

    num //= 10

if has_same_digits:
    print('YES')
else:
    print('NO')