# Challenge 2
# Create:
# 10
# 20
# 30
# 40
# Remove the first element and print:
# Removed: 10
# Queue: deque([20, 30, 40])

from collections import deque

queue = deque([10, 20, 30, 40])

removed = queue.popleft()

print("Removed:", removed)
print("Queue:", queue)