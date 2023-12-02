# объявление функции
def is_password_good(password):
    if len(password) < 8 or password.lower() == password or \
       password.upper() == password or password.isalpha():
        return False

    return True

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
