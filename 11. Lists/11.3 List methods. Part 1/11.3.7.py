n = int(input())
lst = []

for _ in range(n):
    x = int(input())
    lst.append(x)

del lst[1::2]

print(lst)