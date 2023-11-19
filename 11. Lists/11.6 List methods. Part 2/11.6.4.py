n = input()
n = int(n[1:])

for i in range(n):
    s = input()

    if '#' in s:
        pos = s.find('#')
        s = s[:pos].rstrip()

    print(s)