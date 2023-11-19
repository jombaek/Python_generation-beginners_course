text = input().lower().split()
cnt = text.count('a') + text.count('an') + text.count('the')

print(f'Общее количество артиклей: {cnt}')