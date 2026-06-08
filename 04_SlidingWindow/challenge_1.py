# Challenge 1
# nums = [5, 1, 8, 2, 4]
# k = 2

# Find the maximum window sum.

nums = [5, 1, 8, 2, 4]
k = 2

window_sum = sum(nums[:k])  # 5 + 1 = 6
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)