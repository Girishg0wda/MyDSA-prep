numbers = [4, 7, 2, 9, 1]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)