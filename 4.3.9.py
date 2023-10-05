a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a2 < a1:
    a1, b1, a2, b2 = a2, b2, a1, b1

if b1 < a2:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif b1 < b2:
    print(a2, b1)
else:
    print(a2, b2)