genetic_code = input().lower()

adenine = genetic_code.count('а')
guanine = genetic_code.count('г')
cytosine = genetic_code.count('ц')
thymine = genetic_code.count('т')

print('Аденин:', adenine)
print('Гуанин:', guanine)
print('Цитозин:', cytosine)
print('Тимин:', thymine)