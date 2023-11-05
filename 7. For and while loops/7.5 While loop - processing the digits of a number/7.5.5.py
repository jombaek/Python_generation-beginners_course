num = int(input())

while num > 9:
    digit = num % 10
    num //= 10

print(digit)