nums = [2, 4, 6, 8, 10]
k = 2

window_sum = sum(nums[:k])
print(window_sum / k)

for i in range(k, len(nums)):
    window_sum += nums[i]
    window_sum -= nums[i - k]

    print(window_sum / k)