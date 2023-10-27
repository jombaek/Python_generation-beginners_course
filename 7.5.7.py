num = int(input())
is_ordered = True
last_digit = num % 10

while num:
    cur_digit = num % 10

    if last_digit > cur_digit:
        is_ordered = False

    last_digit = cur_digit
    num //= 10

if is_ordered:
    print('YES')
else:
    print('NO')