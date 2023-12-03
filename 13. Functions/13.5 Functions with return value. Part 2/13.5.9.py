# объявление функции
def convert_to_python_case(text):
    res = ''

    for i in range(len(text)):
        if i == 0:
            res += text[i].lower()
        elif text[i].isupper():
            res += '_' + text[i].lower()
        else:
            res += text[i]

    return res

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
