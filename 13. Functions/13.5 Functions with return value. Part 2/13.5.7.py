def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def is_even(num):
    return num % 2 == 0

# объявление функции
def is_valid_password(password):
    password = [int(num) for num in password.split(':')]

    if len(password) == 3:
        a, b, c = password[0], password[1], password[2]

        return is_palindrome(a) and is_prime(b) and is_even(c)

    return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
