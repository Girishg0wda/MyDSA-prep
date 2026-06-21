nums = [3, 2, 4]
target = 6

seen = {}

for i, num in enumerate(nums):
    needed = target - num

    if needed in seen:
        print([seen[needed], i])

    seen[num] = i