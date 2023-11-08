s = input()
cnt_f = s.count('f')


if cnt_f >= 2:
    print(s.find('f'), s.rfind('f'))
elif cnt_f == 1:
    print(s.find('f'))
else:
    print('NO')