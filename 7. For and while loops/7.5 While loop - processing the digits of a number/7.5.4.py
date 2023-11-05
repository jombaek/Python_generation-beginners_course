num = int(input())
sm, count, product, last_digit = 0, 0, 1, num % 10

while num:
    digit = num % 10

    count += 1
    sm += digit
    product *= digit
    first_digit = num
    
    num //= 10

print(sm, count, product, sm / count, first_digit, first_digit + last_digit,  sep='\n')