m, n = int(input()), int(input())

for i in range(m + m % 2 - 1, n - 1, -2):
    print(i)