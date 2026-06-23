# Queues

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

This means the first element inserted into the queue is the first element removed.

## FIFO Principle

**FIFO = First In, First Out**

Example:

```text
Front -> 10 -> 20 -> 30 <- Rear
```

* 10 entered first, so it leaves first.
* 30 entered last, so it leaves last.

## Operations

### Enqueue

Adds an element to the rear of the queue.

```python
queue.append(x)
```

### Dequeue

Removes an element from the front of the queue.

```python
queue.popleft()
```

## Example

```text
Initial Queue:
10 -> 20 -> 30

Enqueue(40):
10 -> 20 -> 30 -> 40

Dequeue():
20 -> 30 -> 40
```

## Applications

* Breadth-First Search (BFS)
* Printer Queue Management
* Task Scheduling
* Customer Service Systems
* CPU Scheduling
* Network Packet Processing

## Time Complexity

| Operation         | Complexity |
| ----------------- | ---------- |
| Enqueue (append)  | O(1)       |
| Dequeue (popleft) | O(1)       |
| Front Access      | O(1)       |

## Python Implementation

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

queue.popleft()
```

## Key Points

* Queue follows the FIFO principle.
* Insertion occurs at the rear.
* Deletion occurs at the front.
* Python's `collections.deque` provides efficient queue operations.
* Widely used in scheduling, buffering, and graph traversal algorithms.

