n = int(input())
negatives_numbers = []
zeros_numbers = []
positives_numbers = []

for _ in range(n):
    x = int(input())
    
    if x < 0:
        negatives_numbers.append(x)
    elif x > 0:
        positives_numbers.append(x)
    else:
        zeros_numbers.append(x)

print(*negatives_numbers, sep='\n')
print(*zeros_numbers, sep='\n')
print(*positives_numbers, sep='\n')