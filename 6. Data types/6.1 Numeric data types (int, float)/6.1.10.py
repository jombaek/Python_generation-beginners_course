n = int(input())
third_digit = n % 10
second_digit = n % 100 // 10
first_digit = n // 100
max_num = max(first_digit, second_digit, third_digit)
min_num = min(first_digit, second_digit, third_digit)
middle_num = first_digit + second_digit + third_digit - max_num - min_num

if max_num - min_num == middle_num:
    print('Число интересное')
else:
    print('Число неинтересное')