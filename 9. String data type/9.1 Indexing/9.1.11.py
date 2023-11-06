n = int(input())
res = ''

while n:
    res = str(n % 2) + res
    n //= 2

print(res)