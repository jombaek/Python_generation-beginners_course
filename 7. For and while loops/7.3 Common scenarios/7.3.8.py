n = int(input())
res = 0

for i in range(n + 1):
    res += (-1) ** (i + 1) * i

print(res)