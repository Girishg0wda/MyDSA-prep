# Challenge 2
# nums = [2, 4, 6, 3, 5]
# k = 3

# Count windows whose sum is greater than 10.

nums = [2, 4, 6, 3, 5]
k = 3

window_sum = sum(nums[:k])
count = 0

if window_sum > 10:
    count += 1

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]

    if window_sum > 10:
        count += 1

print(count)