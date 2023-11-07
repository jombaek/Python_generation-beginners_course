s = input()
n = len(s)
mid = n // 2 + n % 2    # (n + 1) // 2

print(s[mid:] + s[:mid])