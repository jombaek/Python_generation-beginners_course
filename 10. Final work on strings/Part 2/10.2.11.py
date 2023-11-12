s = input()
first_f = s.find('h')
last_f = s.rfind('h')

print(s[:first_f + 1] + s[last_f - 1:first_f:-1] + s[last_f:])