numbers = [int(num) for num in input().split()]

print(*numbers, sep='+', end='=')
print(sum(numbers))
