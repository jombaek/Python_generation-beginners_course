n = int(input())
fact = 1
sum_fact = 0

for i in range(1, n + 1):
    fact *= i
    sum_fact += fact

print(sum_fact)