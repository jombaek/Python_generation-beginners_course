s = input()
most_common = s[0]

for c in s:
    if s.count(c) >= s.count(most_common):
        most_common = c

print(most_common)