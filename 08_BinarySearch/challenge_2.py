# Challenge 2
# nums = [2, 5, 8, 12, 16]
# target = 11
# Print:
# False

nums = [2, 5, 8, 12, 16]
target = 11

left = 0
right = len(nums) - 1

found = False

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        found = True
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print(found)