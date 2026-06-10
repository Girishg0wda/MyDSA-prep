# Challenge 1 
# Create a queue with: Alice Bob Charlie
# Serve everyone.

from collections import deque

queue = deque(["Alice", "Bob", "Charlie"])

while queue:
    print("Served:", queue.popleft())