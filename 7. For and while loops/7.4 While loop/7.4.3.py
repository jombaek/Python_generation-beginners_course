word = input()
count = 0

while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    count += 1
    word = input()

print(count)