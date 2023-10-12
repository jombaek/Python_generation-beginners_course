a, b, c = input(), input(), input()
len_a, len_b, len_c = len(a), len(b), len(c)

if (2 * len_a - len_b - len_c) * (2 * len_b - len_a - len_c) * (2 * len_c - len_b - len_a) == 0:
    print('YES')
else:
    print('NO')