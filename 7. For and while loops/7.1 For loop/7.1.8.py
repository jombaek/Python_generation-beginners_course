from math import pow

m, p, n = int(input()), int(input()), int(input())

for i in range(1, n + 1):
    print(i, m * pow(1 + p / 100, i - 1))