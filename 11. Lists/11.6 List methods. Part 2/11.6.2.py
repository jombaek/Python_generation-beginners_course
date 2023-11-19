numbers = []

for num in input().split():
    numbers.append(int(num))

max_num_idx = numbers.index(max(numbers))
min_num_idx = numbers.index(min(numbers))
numbers[max_num_idx], numbers[min_num_idx] = numbers[min_num_idx], numbers[max_num_idx]

print(*numbers)