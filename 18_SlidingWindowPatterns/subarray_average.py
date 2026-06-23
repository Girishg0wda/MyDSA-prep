nums = [1, 2, 3, 4, 5]
k = 2

window_sum = sum(nums[:k])

print(window_sum / k)

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    print(window_sum / k)