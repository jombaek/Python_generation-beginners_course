n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

func_seq = []

for num in numbers:
    func_seq.append(num ** 2 + 2 * num + 1)

print(*numbers, sep='\n')
print()
print(*func_seq, sep='\n')