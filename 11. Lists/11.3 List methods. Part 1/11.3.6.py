n = int(input())
lst = []
prev = int(input())

for _ in range(n - 1):
    cur = int(input())

    lst.append(prev + cur)
    prev = cur

print(lst)