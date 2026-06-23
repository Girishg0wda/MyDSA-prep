# 1. Hash Map / Set

## Use When

```text
Fast lookup needed
Duplicates
Frequency counting
Pairs
Membership checking
```

## Common Problems

```text
Two Sum
Contains Duplicate
Valid Anagram
Group Anagrams
Longest Consecutive Sequence
```

## Template

```python
seen = {}

for x in nums:
    if condition:
        return answer

    seen[x] = True
```

## Complexity

```text
Time: O(n)
Space: O(n)
```

---

# 2. Two Pointers

## Use When

```text
Sorted array
Pairs
Triplets
Palindrome
Opposite-end scanning
```

## Common Problems

```text
Two Sum II
Container With Most Water
3Sum
Valid Palindrome
Remove Duplicates
```

## Template

```python
left = 0
right = len(arr) - 1

while left < right:

    if condition:
        left += 1
    else:
        right -= 1
```

## Complexity

```text
Time: O(n)
Space: O(1)
```

---

# 3. Sliding Window

## Use When

```text
Subarray
Substring
Contiguous segment
Longest
Shortest
Maximum
Minimum
```

## Common Problems

```text
Longest Substring Without Repeating Characters
Maximum Sum Subarray
Minimum Window Substring
Permutation in String
```

## Template

```python
left = 0

for right in range(len(nums)):

    while invalid_window:
        left += 1

    update_answer()
```

## Complexity

```text
Time: O(n)
Space: O(k)
```

---

# 4. Binary Search

## Use When

```text
Sorted data
Search space
Find minimum
Find maximum
Answer optimization
```

## Common Problems

```text
Binary Search
Search Rotated Array
Koko Eating Bananas
Capacity To Ship Packages
```

## Template

```python
low = 0
high = n

while low <= high:

    mid = (low + high) // 2

    if valid(mid):
        high = mid - 1
    else:
        low = mid + 1
```

## Complexity

```text
Time: O(log n)
Space: O(1)
```

---

# 5. Greedy

## Use When

```text
Local best choice
Intervals
Scheduling
Deadlines
Profit maximization
```

## Common Problems

```text
Activity Selection
Jump Game
Gas Station
Non-overlapping Intervals
Fractional Knapsack
```

## Template

```python
items.sort()

for item in items:

    if can_choose(item):
        choose(item)
```

## Complexity

```text
Usually O(n log n)
```

---

# 6. Heap / Priority Queue

## Use When

```text
Repeated min/max extraction
Top K
Scheduling
Merging
```

## Common Problems

```text
Kth Largest Element
Top K Frequent Elements
Merge K Sorted Lists
Task Scheduler
```

## Template

```python
import heapq

heap = []

heapq.heappush(heap, x)

smallest = heapq.heappop(heap)
```

## Complexity

```text
Push: O(log n)
Pop: O(log n)
```

---

# 7. Intervals

## Use When

```text
Meetings
Schedules
Ranges
Bookings
Time windows
```

## Common Problems

```text
Merge Intervals
Insert Interval
Meeting Rooms
Erase Overlap Intervals
```

## Template

```python
intervals.sort()

for interval in intervals:
    process(interval)
```

## Complexity

```text
Time: O(n log n)
```

---

# 8. Stack

## Use When

```text
Matching symbols
Undo operations
Monotonic processing
Nearest greater/smaller
```

## Common Problems

```text
Valid Parentheses
Daily Temperatures
Largest Rectangle Histogram
Min Stack
```

## Template

```python
stack = []

for x in nums:

    while stack and condition:
        stack.pop()

    stack.append(x)
```

## Complexity

```text
Time: O(n)
```

---

# 9. Queue / BFS

## Use When

```text
Shortest path (unweighted)
Level traversal
Minimum steps
Multi-source expansion
```

## Common Problems

```text
Binary Tree Level Order
Rotting Oranges
Word Ladder
Number of Islands (BFS)
```

## Template

```python
from collections import deque

q = deque([start])

while q:

    node = q.popleft()

    for nei in neighbors:
        q.append(nei)
```

## Complexity

```text
Time: O(V + E)
```

---

# 10. DFS / Backtracking

## Use When

```text
Explore all possibilities
Permutations
Combinations
Paths
Decision trees
```

## Common Problems

```text
Subsets
Permutations
Combination Sum
N Queens
Word Search
```

## Template

```python
def dfs(path):

    if complete:
        answer.append(path[:])
        return

    for choice in choices:

        path.append(choice)

        dfs(path)

        path.pop()
```

## Complexity

```text
Usually Exponential
```

---

# 11. Trees

## Use When

```text
Hierarchical data
Parent-child relationships
Recursive structure
```

## Traversals

```text
Preorder
Inorder
Postorder
Level Order
```

## Common Problems

```text
Maximum Depth
Diameter
Balanced Tree
Lowest Common Ancestor
```

## Complexity

```text
Time: O(n)
```

---

# 12. Graphs

## Use When

```text
Connections
Networks
Dependencies
Routes
```

## Algorithms

```text
DFS
BFS
Topological Sort
Union Find
Dijkstra
```

## Common Problems

```text
Course Schedule
Clone Graph
Number of Provinces
Network Delay Time
```

## Complexity

```text
Typically O(V + E)
```

---

# 13. Dynamic Programming

## Use When

```text
Optimal answer
Overlapping subproblems
Repeated computations
```

## Common Problems

```text
House Robber
Coin Change
LCS
Knapsack
Unique Paths
```

## Template

```python
dp = [...]

for state in states:
    dp[state] = transition(...)
```

## Complexity

```text
State Count × Transition Cost
```

---

# 14. Union Find (DSU)

## Use When

```text
Connectivity
Cycle detection
Dynamic graph components
```

## Common Problems

```text
Number of Provinces
Redundant Connection
Accounts Merge
```

## Operations

```python
find(x)
union(x, y)
```

## Complexity

```text
Almost O(1)
```

---

# Pattern Recognition Guide

```text
Duplicates/Frequency
    → Hash Map

Pair in Sorted Array
    → Two Pointers

Subarray/Substring
    → Sliding Window

Sorted Search Space
    → Binary Search

Intervals/Scheduling
    → Greedy

Top K
    → Heap

Matching Symbols
    → Stack

Shortest Path (Unweighted)
    → BFS

Explore All Possibilities
    → Backtracking

Optimal Answer
    → Dynamic Programming

Connectivity
    → Union Find

Trees
    → DFS/BFS Tree Traversal

Graphs
    → DFS/BFS/Dijkstra/Topo Sort
```

# Interview Strategy

```text
1. Identify Pattern
2. Pick Data Structure
3. State Complexity
4. Write Brute Force
5. Optimize
6. Verify Edge Cases
7. Code Cleanly
```
