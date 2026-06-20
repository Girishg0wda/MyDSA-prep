coins = [10, 5, 2, 1]
amount = 18

count = 0

for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1

print(count)