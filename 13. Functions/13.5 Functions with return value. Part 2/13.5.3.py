def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# объявление функции
def get_next_prime(num):
    cur_num = num + 1

    while not is_prime(cur_num):
        cur_num += 1

    return cur_num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
