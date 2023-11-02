a, b = int(input()), int(input())
max_sum_of_divisors = 0
res = 0

for i in range(a, b + 1):
    total_sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total_sum += j
    
    if total_sum >= max_sum_of_divisors:
        max_sum_of_divisors = total_sum
        res = i

print(res, max_sum_of_divisors)