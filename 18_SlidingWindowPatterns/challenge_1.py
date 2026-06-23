# Find maximum sum window.
# nums = [4, 2, 1, 7, 8]
# k = 2
# Expected:
# 15
# Because:
# 7 + 8 = 15

nums = [4, 2, 1, 7, 8]
k = 2

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)