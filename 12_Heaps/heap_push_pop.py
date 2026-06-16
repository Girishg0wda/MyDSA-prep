import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

print("Heap:", heap)

smallest = heapq.heappop(heap)

print("Removed:", smallest)
print("Heap after pop:", heap)