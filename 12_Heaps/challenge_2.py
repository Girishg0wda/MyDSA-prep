import heapq

nums = [7, 3, 9, 1, 4]

heapq.heapify(nums)

print(heapq.heappop(nums))
print(heapq.heappop(nums))