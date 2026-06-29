# Mini Challenge 2
# Find first occurrence.
# nums = [1, 3, 3, 3, 5]
# target = 3
# Expected:
# 1


nums = [1, 3, 3, 3, 5]
target = 3

left = 0
right = len(nums) - 1
answer = -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        answer = mid
        right = mid - 1
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(answer)