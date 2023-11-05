n = int(input())
total = 0
sum_of_digit = 0

while n:
    sum_of_digit += n % 10
    n //= 10

    if n == 0:
        if sum_of_digit < 10:
            break
        n = sum_of_digit
        sum_of_digit = 0

print(sum_of_digit)