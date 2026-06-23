nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)