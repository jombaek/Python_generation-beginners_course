s = input()
count_vowels = 0
count_consonants = 0
vowels = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'

for c in s:
    if c in vowels:
        count_vowels += 1
    elif c in consonants:
        count_consonants += 1

print('Количество гласных букв равно', count_vowels)
print('Количество согласных букв равно', count_consonants)