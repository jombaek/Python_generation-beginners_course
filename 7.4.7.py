price = int(input())
coins = 0

while price >= 25:
    price -= 25
    coins += 1

while price >= 10:
    price -= 10
    coins += 1

while price >= 5:
    price -= 5
    coins += 1
    
while price >= 1:
    price -= 1
    coins += 1

print(coins)