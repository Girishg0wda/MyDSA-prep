# Challenge 1
# nums = [1, 4, 6, 8, 10, 15]
# target = 10
# Print the index.

nums = [1, 4, 6, 8, 10, 15]
target = 10

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