number = input().split('-')
lens = [len(el) for el in number]

if lens == [1, 3, 3, 4] and ''.join(number).isdigit() and number[0] == '7' or \
   lens == [3, 3, 4] and ''.join(number).isdigit():
    print('YES')
else:
    print('NO')
