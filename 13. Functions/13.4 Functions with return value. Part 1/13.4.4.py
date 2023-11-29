def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# объявление функции
def number_of_factors(num):
    return len(get_factors(num))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
