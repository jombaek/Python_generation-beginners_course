n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

max_num_idx = 0
min_num_idx = 0

for i in range(n):
    if numbers[i] > numbers[max_num_idx]:
        max_num_idx = i
    if numbers[i] < numbers[min_num_idx]:
        min_num_idx = i

del numbers[max(max_num_idx, min_num_idx)]
del numbers[min(max_num_idx, min_num_idx)]

print(*numbers, sep='\n')