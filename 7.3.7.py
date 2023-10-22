n = int(input())
sm = 0

for i in range(1, n + 1):
    if n % i == 0:
        sm += i

print(sm)