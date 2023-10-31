n = int(input())

for i in range(n):
    for j in range(i + 1):
        if i + j >= n:
            break
        print('*', end='')
    print()