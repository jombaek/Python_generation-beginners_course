numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers.sort()
print(*numbers)
numbers.reverse()
print(*numbers)