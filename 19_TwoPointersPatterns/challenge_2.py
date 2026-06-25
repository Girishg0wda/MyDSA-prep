# Find two numbers in:
# nums = [1, 2, 4, 6, 10]
# target = 8
# Expected:
# [1, 3]
# Because:
# 2 + 6 = 8

nums = [1, 2, 4, 6, 10]
target = 8

left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        print([left, right])
        break
    elif total < target:
        left += 1
    else:
        right -= 1