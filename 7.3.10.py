is_all_even = True

for _ in range(10):
    x = int(input())
    if x % 2 != 0:
        is_all_even = False

if is_all_even:
    print('YES')
else:
    print('NO')