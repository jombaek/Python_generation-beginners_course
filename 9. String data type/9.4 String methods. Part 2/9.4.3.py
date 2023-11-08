n = int(input())
cnt = 0

for _ in range(n):
    message = input()

    if message.count('11') >= 3:
        cnt += 1

print(cnt)