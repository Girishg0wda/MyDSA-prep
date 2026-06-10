from collections import deque

queue = deque()

queue.append("Document1")
queue.append("Document2")
queue.append("Document3")

while queue:
    print("Printing:", queue.popleft())