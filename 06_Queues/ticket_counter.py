from collections import deque

queue = deque(["Rahul", "Priya", "Amit"])

served = queue.popleft()

print("Served:", served)
print("Remaining:", queue)