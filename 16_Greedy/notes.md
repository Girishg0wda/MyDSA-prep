# Greedy Algorithms

Greedy Algorithms solve problems by making the best possible local choice at every step.

The idea is:

```text
Choose the best option now
↓
Never reconsider it
↓
Reach a solution
```

Unlike Dynamic Programming, Greedy does not explore multiple possibilities.

---

# Core Idea

A Greedy algorithm works when:

### 1. Greedy Choice Property

A globally optimal solution can be obtained by making a locally optimal choice.

Example:

```text
Activity Selection

Choose the activity
that finishes earliest.
```

The first best choice leads to the optimal answer.

---

### 2. Optimal Substructure

An optimal solution contains optimal solutions to its subproblems.

Example:

```text
After choosing one activity,
the remaining problem is still
an activity selection problem.
```

---

# General Greedy Framework

```python
def greedy(items):

    sort(items)

    answer = []

    for item in items:

        if can_choose(item):
            answer.append(item)

    return answer
```

---

# Greedy Problem Solving Framework

Whenever you see a Greedy problem:

### Step 1: Identify the Goal

Ask:

```text
What am I trying to optimize?
```

Examples:

```text
Maximum activities
Minimum cost
Maximum profit
Minimum intervals
```

---

### Step 2: Find a Local Best Choice

Ask:

```text
What is the best decision
I can make right now?
```

Examples:

```text
Earliest finish time
Largest value
Smallest cost
Highest profit
```

---

### Step 3: Prove Correctness

Ask:

```text
Does choosing this option
ever hurt the final answer?
```

If yes:

```text
Greedy may fail.
```

If no:

```text
Greedy works.
```

---

# Example 1: Activity Selection

Problem:

```text
Select maximum number
of non-overlapping activities.
```

Activities:

```text
Start = [1,3,0,5,8,5]
End   = [2,4,6,7,9,9]
```

Greedy Rule:

```text
Always choose the activity
with the earliest finish time.
```

Solution:

```python
activities.sort(key=lambda x: x[1])

count = 1
last_end = activities[0][1]

for start, end in activities:

    if start >= last_end:

        count += 1
        last_end = end
```

### Complexity

```text
Time: O(n log n)
Space: O(1)
```

---

# Example 2: Fractional Knapsack

Problem:

```text
Maximize value inside a bag
with limited capacity.
```

Items:

```text
weight
value
```

Greedy Rule:

```text
Pick item with highest
value/weight ratio first.
```

Sort:

```python
items.sort(
    key=lambda x: x.value / x.weight,
    reverse=True
)
```

Take fractions if needed.

### Complexity

```text
Time: O(n log n)
Space: O(1)
```

---

# Example 3: Minimum Number of Coins

Coins:

```text
[1, 2, 5, 10, 20, 50, 100]
```

Amount:

```text
93
```

Greedy:

```text
Take largest coin possible.
```

Example:

```text
93

50
20
20
2
1
```

Answer:

```text
5 coins
```

Works for many currency systems.

---

# Example 4: Huffman Coding

Problem:

```text
Build optimal prefix codes.
```

Greedy Rule:

```text
Always combine
the two smallest frequencies.
```

Implementation:

```python
Use a min heap.
```

### Complexity

```text
Time: O(n log n)
Space: O(n)
```

---

# Example 5: Jump Game

Problem:

```text
Can you reach
the last index?
```

Greedy Idea:

```text
Track the farthest position
reachable so far.
```

Solution:

```python
reach = 0

for i in range(len(nums)):

    if i > reach:
        return False

    reach = max(
        reach,
        i + nums[i]
    )

return True
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# When Greedy Fails

Example:

Coin Change

Coins:

```text
[1, 3, 4]
Amount = 6
```

Greedy:

```text
4 + 1 + 1
```

Answer:

```text
3 coins
```

Optimal:

```text
3 + 3
```

Answer:

```text
2 coins
```

Greedy fails.

Dynamic Programming is needed.

---

# Common Greedy Patterns

## Sorting Based

Sort and make decisions.

Examples:

```text
Activity Selection
Meeting Rooms
Merge Intervals
```

---

## Priority Queue (Heap)

Always choose:

```text
Smallest
Largest
Highest Priority
```

Examples:

```text
Huffman Coding
Connect Ropes
Task Scheduling
```

---

## Interval Problems

Sort intervals and process.

Examples:

```text
Non-overlapping Intervals
Insert Interval
Meeting Rooms
```

---

## Resource Allocation

Examples:

```text
Fractional Knapsack
Job Scheduling
CPU Scheduling
```

---

# Greedy vs Dynamic Programming

| Feature             | Greedy            | DP                            |
| ------------------- | ----------------- | ----------------------------- |
| Decision            | Best local choice | Explore all important choices |
| Stores Results      | No                | Yes                           |
| Reconsiders Choices | No                | Yes                           |
| Speed               | Faster            | Usually slower                |
| Memory              | Low               | Higher                        |
| Optimal Guarantee   | Not always        | Usually yes                   |

---

# Recognition Pattern

Use Greedy when:

✅ Problem asks for:

```text
Maximum
Minimum
Fewest
Largest
Smallest
```

AND

✅ A local best choice seems obvious.

Common keywords:

```text
Intervals
Scheduling
Deadlines
Profit
Cost
Merge
Optimize
```

---

# Interview Tips

1. Try Greedy first.
2. Identify the local best choice.
3. Ask if the choice can ever be wrong.
4. Prove correctness.
5. If Greedy fails, think DP.
6. Most Greedy solutions involve sorting or heaps.
7. Always justify why Greedy works.

---

# Master Greedy Formula

```text
Goal
↓
Best Local Choice
↓
Make Choice
↓
Never Revisit
↓
Final Solution
```

---

# Quick Revision

```text
Greedy = Best Choice Now

Requirements:
1. Greedy Choice Property
2. Optimal Substructure

Common Techniques:
- Sorting
- Heaps
- Intervals
- Resource Allocation

Advantages:
- Fast
- Simple
- Low Memory

Disadvantages:
- Doesn't always produce optimal answers

Examples:
- Activity Selection
- Fractional Knapsack
- Huffman Coding
- Jump Game
- Job Scheduling
```
