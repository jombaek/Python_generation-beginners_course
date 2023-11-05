a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a > b:
    a = b

if c > d:
    c = d

if a < c:
    print(a)
else:
    print(c)