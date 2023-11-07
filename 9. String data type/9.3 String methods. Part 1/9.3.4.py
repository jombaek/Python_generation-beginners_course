s = input()
cnt = 0

for c in s:
    if c != c.upper():
        cnt += 1

print(cnt)