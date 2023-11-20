n = int(input())
squares_of_numbers = [i ** 2 for i in range(1, n + 1)]

print(*squares_of_numbers, sep='\n')