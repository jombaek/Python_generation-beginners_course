L = input().split()
M = input().split()
n = len(L)

lst = [int(L[i]) + int(M[i]) for i in range(n)]

print(*lst)