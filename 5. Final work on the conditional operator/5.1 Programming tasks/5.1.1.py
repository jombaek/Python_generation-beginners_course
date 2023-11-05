year = int(input())
last_digit = year % 10
pre_last_digit = year % 100 // 10

if last_digit == 0 and pre_last_digit == 0:
    print('YES')
else:
    print('NO')