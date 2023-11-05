from math import log

n = int(input())
res = -log(n)

for i in range(1, n + 1):
    res += 1 / i

print(res)