nums = [1, 2, 3, 1]

seen = set()

duplicate = False

for num in nums:
    if num in seen:
        duplicate = True
        break

    seen.add(num)

print(duplicate)