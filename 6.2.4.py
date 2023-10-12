city1 = input()
city2 = input()
city3 = input()

if len(city1) > len(city2):
    city1, city2 = city2, city1

if len(city2) > len(city3):
    city2, city3 = city3, city2

if len(city1) > len(city2):
    city1, city2 = city2, city1

print(city1, city3, sep='\n')