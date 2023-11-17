n = int(input())
lst = []

for _ in range(n):
    x = input()
    lst.append(x)

k = int(input())
res = ''

for el in lst:
    if len(el) >= k:
        res += el[k - 1]

print(res)