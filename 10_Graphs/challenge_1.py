graph = {
    "A": ["B", "C"],
    "B": [],
    "C": []
}

visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)

    print(node)

    for neighbor in graph[node]:
        dfs(neighbor)

dfs("A")