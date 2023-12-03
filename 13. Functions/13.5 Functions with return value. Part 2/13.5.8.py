# объявление функции
def is_correct_bracket(text):
    cnt = 0

    for c in text:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return cnt == 0

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
