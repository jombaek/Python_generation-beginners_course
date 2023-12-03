# объявление функции
def is_palindrome(text):
    text = [c.lower() for c in text if c not in ' ,.!?-']

    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
