nums = [1, 2, 3, 1]

seen = set()

for num in nums:
    if num in seen:
        print("Duplicate Found")
        break

    seen.add(num)