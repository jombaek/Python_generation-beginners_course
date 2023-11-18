n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

search_query = input().lower()

for el in lst:
    if search_query in el.lower():
        print(el)