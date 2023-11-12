s = input()
first_f = s.find('f')

if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    print(s.find('f', first_f + 1))