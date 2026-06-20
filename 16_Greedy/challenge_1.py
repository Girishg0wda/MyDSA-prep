# Find minimum coins:
# coins = [20, 10, 5, 1]
# amount = 47
# Expected:
# 5
# Because:
# 20 + 20 + 5 + 1 + 1

coins = [20, 10, 5, 1]
amount = 47

count = 0

for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1

print(count)