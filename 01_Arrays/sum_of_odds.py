numbers = [4, 7, 2, 9, 1, 8]

total = 0

for num in numbers:
    if num % 2 == 1:
        total += num

print("Sum of odd numbers:", total)