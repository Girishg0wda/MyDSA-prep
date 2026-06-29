# Mini Challenge 1
# Find insert position.
# nums = [2, 4, 6, 8]
# target = 5
# Expected:
# 2

nums = [2, 4, 6, 8]
target = 5

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
else:
    print(left)