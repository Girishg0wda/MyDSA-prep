# Challenge 3 — Find the Index
# nums = [3, 7, 11, 15, 19, 24, 31]
# target = 19
# Print the index.
# Expected Output
# 4

nums = [3, 7, 11, 15, 19, 24, 31]
target = 19

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print(mid)
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1