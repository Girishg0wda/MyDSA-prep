# Graphs

**Graphs** are non-linear data structures used to represent relationships between objects.

## Components

A graph consists of:

1. **Nodes (Vertices)** – Represent entities or objects.
2. **Edges** – Represent connections between nodes.

## Representations

### Adjacency List

Stores a list of neighboring nodes for each vertex.

Example:

```text
A → B, C
B → A, D
C → A
D → B
```

### Adjacency Matrix

Stores connections in a 2D matrix.

Example:

```text
    A B C D
A [ 0 1 1 0 ]
B [ 1 0 0 1 ]
C [ 1 0 0 0 ]
D [ 0 1 0 0 ]
```

## Traversals

### Depth First Search (DFS)

DFS explores as far as possible along a branch before backtracking.

#### Steps

1. Start from a source node.
2. Visit the node and mark it as visited.
3. Move to an unvisited neighboring node.
4. Repeat until no unvisited neighbors remain.
5. Backtrack and continue exploring.
6. Stop when all reachable nodes are visited.

#### Characteristics

* Uses **recursion** or a **stack**.
* Explores deeply before moving to another branch.
* Useful for path finding and cycle detection.

### Breadth First Search (BFS)

BFS explores nodes level by level.

#### Steps

1. Start from a source node.
2. Add the source node to a queue.
3. Remove a node from the queue and visit it.
4. Add all unvisited neighboring nodes to the queue.
5. Repeat until the queue becomes empty.

#### Characteristics

* Uses a **queue**.
* Explores nodes level by level.
* Finds the shortest path in an unweighted graph.

## Example

Graph:

```text
    A
   / \
  B   C
 / \
D   E
```

### DFS Traversal

```text
A → B → D → E → C
```

### BFS Traversal

```text
A → B → C → D → E
```

## Time Complexity

| Traversal | Time Complexity |
| --------- | --------------- |
| DFS       | O(V + E)        |
| BFS       | O(V + E)        |

Where:

* **V** = Number of vertices
* **E** = Number of edges

## Space Complexity

| Traversal | Space Complexity |
| --------- | ---------------- |
| DFS       | O(V)             |
| BFS       | O(V)             |

## Applications

* Social Networks
* Maps and Navigation Systems
* Network Routing
* Recommendation Systems
* Web Crawlers
* Dependency Resolution

## Key Points

* Graphs represent relationships between entities.
* A graph is made up of **vertices (nodes)** and **edges**.
* Common representations are **Adjacency Lists** and **Adjacency Matrices**.
* **DFS** explores deeply before backtracking.
* **BFS** explores level by level using a queue.
* Both DFS and BFS have a time complexity of **O(V + E)**.

