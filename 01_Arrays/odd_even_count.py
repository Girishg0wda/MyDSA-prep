numbers = [4, 7, 2, 9, 1, 8]

count = 0

for num in numbers:
    if num % 2 == 1:
        count += 1

print("Odd count:", count)