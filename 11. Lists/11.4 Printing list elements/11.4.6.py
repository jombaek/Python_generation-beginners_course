n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

k = int(input())
search_queries = []

for _ in range(k):
    search_queries.append(input().lower())

for el in lst:
    for word in search_queries:
        if word not in el.lower():
            break
    else:
        print(el)