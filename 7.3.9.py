n = int(input())
first_max = -1
second_max = -1

for _ in range(n):
    x = int(input())
    if x > first_max:
        first_max, second_max = x, first_max
    elif x > second_max:
        second_max = x

print(first_max, second_max, sep='\n')