# Day 22 – Interview Pattern (Queue & Monotonic Queue)

## Overview

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

The first element inserted is the first one removed.

Queues are widely used in:

* Breadth-First Search (BFS)
* Scheduling
* Streaming data
* Sliding Window problems
* Producer–Consumer systems

---

# Queue Operations

| Operation  | Description             | Time |
| ---------- | ----------------------- | ---- |
| enqueue(x) | Insert at rear          | O(1) |
| dequeue()  | Remove from front       | O(1) |
| front()    | View first element      | O(1) |
| isEmpty()  | Check if queue is empty | O(1) |

---

# Python Implementation

```python
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

# Front
print(queue[0])

# Dequeue
queue.popleft()

# Check empty
if not queue:
    print("Empty")
```

---

# Queue Visualization

```
Front                     Rear

10 → 20 → 30 → 40

Dequeue

20 → 30 → 40

Enqueue 50

20 → 30 → 40 → 50
```

---

# Queue vs Stack

| Stack | Queue   |
| ----- | ------- |
| LIFO  | FIFO    |
| Push  | Enqueue |
| Pop   | Dequeue |
| Top   | Front   |

---

# When to Think of a Queue

Use a Queue when:

* Processing elements in arrival order
* Performing BFS
* Simulating waiting lines
* Level-order traversal
* Sliding window processing

---

# Breadth-First Search (BFS)

Queue is the core data structure for BFS.

Algorithm:

1. Push starting node into queue.
2. While queue is not empty:

   * Remove front node.
   * Process it.
   * Push all unvisited neighbors.

---

# BFS Template

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

# Level Order Traversal

Tree problems often use a queue.

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

---

# Monotonic Queue

A **Monotonic Queue** maintains its elements in sorted order while supporting efficient insertion and removal.

Types:

* Increasing Queue
* Decreasing Queue

Most interview questions use a **decreasing queue**.

---

# Why Use a Monotonic Queue?

Normal Queue

```
4 2 12 5
```

Maximum cannot be found efficiently.

Monotonic Queue

```
12 5
```

The maximum is always at the front.

---

# Sliding Window Maximum

Problem

```
nums = [1,3,-1,-3,5,3,6,7]

k = 3
```

Output

```
[3,3,5,5,6,7]
```

---

# Sliding Window Maximum Template

```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    ans = []

    for i in range(len(nums)):

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            ans.append(nums[dq[0]])

    return ans
```

---

# Time Complexity

Normal Approach

```
O(n × k)
```

Monotonic Queue

```
O(n)
```

Each element enters and leaves the deque at most once.

---

# Recognition Checklist

Think Queue when:

* BFS
* Level-order traversal
* Scheduling
* Streaming data
* First-in, first-out processing

Think Monotonic Queue when:

* Sliding window maximum/minimum
* Window size is fixed
* Need O(n) optimization
* Need current maximum or minimum quickly

---

# Common Queue Problems

## Easy

* Implement Queue using Stacks
* Number of Recent Calls
* Moving Average from Data Stream

---

## Medium

* Binary Tree Level Order Traversal
* Rotting Oranges
* Number of Islands (BFS)
* Open the Lock
* Sliding Window Maximum

---

## Hard

* Shortest Path in Binary Matrix
* Bus Routes
* Word Ladder
* Minimum Jumps to Reach Home

---

# Complexity

| Operation              | Time     |
| ---------------------- | -------- |
| Enqueue                | O(1)     |
| Dequeue                | O(1)     |
| Front                  | O(1)     |
| BFS                    | O(V + E) |
| Sliding Window Maximum | O(n)     |

---

# Common Mistakes

### Mistake 1

Using a list instead of `deque`.

Wrong

```python
queue.pop(0)
```

Time Complexity

```
O(n)
```

Correct

```python
queue.popleft()
```

Time Complexity

```
O(1)
```

---

### Mistake 2

Forgetting to remove expired indices in sliding window problems.

Always remove indices that are outside the current window.

---

### Mistake 3

Not marking nodes as visited before enqueueing them in BFS.

This may cause duplicate processing.

---

# Interview Tips

* Queue almost always indicates **BFS**.
* Use `collections.deque` in Python for efficient queue operations.
* For sliding window maximum/minimum, think **Monotonic Queue** instead of recalculating every window.
* Remember that each element is inserted and removed at most once in a monotonic queue.

---

# Quick Revision

## Queue

Used For

* BFS
* Level-order traversal
* Scheduling
* Streaming
* FIFO processing

Time

```
Enqueue : O(1)
Dequeue : O(1)
```

---

## Monotonic Queue

Used For

* Sliding Window Maximum
* Sliding Window Minimum
* Fixed-size window optimization

Time

```
O(n)
```

---

# Key Takeaways

✅ Queue follows **FIFO (First In, First Out)**.

✅ Use `deque` in Python for efficient queue operations.

✅ BFS is implemented using a queue.

✅ A Monotonic Queue maintains useful order while processing a sliding window.

✅ Sliding Window Maximum can be solved in **O(n)** using a Monotonic Queue instead of **O(n × k)**.
