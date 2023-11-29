# объявление функции
def quick_merge(list1, list2):
    n = len(list1)
    m = len(list2)
    i, j = 0, 0
    result = []

    while i < n and j < m:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    if i < n:
        result.extend(list1[i:])

    if j < m:
        result.extend(list2[j:])

    return result

# считываем данные
n = int(input())
numbers = []

for _ in range(n):
    numbers.append([int(c) for c in input().split()])

while len(numbers) >= 2:
    list1 = numbers.pop(0)
    list2 = numbers.pop(0)

    numbers.append(quick_merge(list1, list2))

# вызываем функцию
print(*numbers[0])
