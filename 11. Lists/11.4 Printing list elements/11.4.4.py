n = int(input())
lst = []

for _ in range(n):
    x = input()
    if x not in lst:
        lst.append(x)

print(*lst, sep='\n')