s = input()
count_plus = 0
count_multiply = 0

for c in s:
    if c == '+':
        count_plus += 1
    elif c == '*':
        count_multiply += 1

print('Символ + встречается', count_plus, 'раз')
print('Символ * встречается', count_multiply, 'раз')