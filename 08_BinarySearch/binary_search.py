nums = [2, 5, 8, 12, 16, 23, 38]
target = 23

left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        print("Found!")
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1