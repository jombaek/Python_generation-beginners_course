s = input()
digit_count = 0

for i in range(10):
    digit_count += s.count(str(i))

print(digit_count)