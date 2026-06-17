nums = [5, 2, 8, 1, 3]

n = len(nums)

for i in range(n):
    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)