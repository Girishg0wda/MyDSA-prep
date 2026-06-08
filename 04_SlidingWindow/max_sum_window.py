nums = [1, 2, 3, 4, 5]
k = 3

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i - k]

    max_sum = max(max_sum, window_sum)

print("Maximum window sum:", max_sum)