numbers = [int(num) for num in input().split()]
cubes_of_numbers = [num ** 3 for num in numbers]

for cube in cubes_of_numbers:
    print(cube, end=' ')