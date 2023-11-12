s = input()
n = len(s)

for i in range(n):
    if i % 3 == 0:
        continue
    print(s[i], end='')