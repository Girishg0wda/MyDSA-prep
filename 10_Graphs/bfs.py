from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}

queue = deque(["A"])
visited = {"A"}

while queue:
    node = queue.popleft()

    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)