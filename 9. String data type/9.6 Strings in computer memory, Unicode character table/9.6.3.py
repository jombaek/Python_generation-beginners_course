n = int(input())
s = input()

for c in s:
    cur_n = ord('a') + (ord(c) - ord('a') + 26 - n) % 26
    print(chr(cur_n), end='')