# объявление функции
def merge(list1, list2):
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
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
