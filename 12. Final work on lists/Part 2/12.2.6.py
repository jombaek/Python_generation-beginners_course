words = [word[1:] + word[0] + 'ки' for word in input().split()]

print(*words)
