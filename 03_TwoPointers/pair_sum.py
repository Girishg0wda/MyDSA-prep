nums = [1, 2, 3, 4, 5]
target = 9

left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        print("Pair found:", nums[left], nums[right])
        break

    elif total < target:
        left += 1

    else:
        right -= 1