# Heaps

A **Heap** is a special tree-based data structure that satisfies the **heap property**.

A heap is typically implemented using an array and is commonly used for efficient priority-based operations.

---

## Types of Heaps

### Min Heap

In a Min Heap, the parent node is always smaller than or equal to its children.

```text
      1
     / \
    3   5
   / \
  7   9
```

- Smallest element is at the root.
- Python's `heapq` implements a Min Heap by default.

---

### Max Heap

In a Max Heap, the parent node is always greater than or equal to its children.

```text
      9
     / \
    7   5
   / \
  3   1
```

- Largest element is at the root.

---

## Heap Representation

A heap is usually stored as an array.

Example:

```text
      1
     / \
    3   5
   / \
  7   9
```

Array Representation:

```python
[1, 3, 5, 7, 9]
```

For an element at index `i`:

```text
Left Child  = 2*i + 1
Right Child = 2*i + 2
Parent      = (i - 1) // 2
```

---

## Python Heap Library

```python
import heapq
```

Python provides the `heapq` module for heap operations.

---

## Heap Operations

### 1. heapify()

Converts a list into a heap.

```python
import heapq

nums = [4, 7, 1, 3, 9]
heapq.heapify(nums)

print(nums)
```

Output:

```python
[1, 3, 4, 7, 9]
```

**Time Complexity:** O(n)

---

### 2. heappush()

Adds an element to the heap.

```python
heapq.heappush(nums, 2)
```

**Time Complexity:** O(log n)

---

### 3. heappop()

Removes and returns the smallest element.

```python
smallest = heapq.heappop(nums)

print(smallest)
```

**Time Complexity:** O(log n)

---

### 4. Peek Minimum Element

Access the root element.

```python
nums[0]
```

**Time Complexity:** O(1)

---

## Max Heap in Python

Since `heapq` supports only Min Heap, use negative values.

```python
import heapq

nums = [4, 7, 1, 3]

max_heap = [-x for x in nums]
heapq.heapify(max_heap)

largest = -heapq.heappop(max_heap)

print(largest)
```

Output:

```python
7
```

---

## Common Heap Patterns

### K Smallest Elements

```python
import heapq

nums = [5, 2, 8, 1, 9]

print(heapq.nsmallest(3, nums))
```

Output:

```python
[1, 2, 5]
```

---

### K Largest Elements

```python
import heapq

nums = [5, 2, 8, 1, 9]

print(heapq.nlargest(2, nums))
```

Output:

```python
[9, 8]
```

---

## Applications of Heaps

- Priority Queue
- Task Scheduling
- Dijkstra's Algorithm
- Prim's Algorithm
- Huffman Coding
- Heap Sort
- Top K Problems
- Median of Data Stream
- Merge K Sorted Lists

---

## Time Complexities

| Operation | Complexity |
|------------|------------|
| heapify() | O(n) |
| heappush() | O(log n) |
| heappop() | O(log n) |
| Peek Root | O(1) |
| Build Heap | O(n) |

---

## Advantages

- Efficient insertion and deletion.
- Fast access to minimum/maximum element.
- Useful for priority-based processing.
- Space-efficient array representation.

---

## Disadvantages

- Searching for arbitrary elements is O(n).
- Not suitable for ordered traversal.
- More complex than simple arrays or lists.

---

## Heap vs Binary Search Tree

| Feature | Heap | BST |
|----------|------|------|
| Root Element | Min/Max | Depends |
| Search | O(n) | O(log n) Average |
| Insert | O(log n) | O(log n) Average |
| Delete Root | O(log n) | O(log n) Average |
| Priority Queue | Excellent | Not Ideal |

---

## Key Points

- Heap is a complete binary tree.
- Min Heap stores the smallest element at the root.
- Max Heap stores the largest element at the root.
- Python provides heap support through `heapq`.
- `heapify()` builds a heap in O(n).
- Insertion and deletion take O(log n).
- Heaps are widely used in Priority Queues and Graph Algorithms.
