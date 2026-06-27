# Day 19 – Interview Patterns (Two Pointers & Sliding Window)

## Overview

Today focuses on two of the most frequently used coding interview patterns:

* Two Pointers
* Sliding Window

Learning these patterns helps solve many array and string problems in **O(n)** time instead of **O(n²)**.

---

# Two Pointers Pattern

## Used For

* Sorted Arrays
* Palindromes
* Pair Sum Problems
* Array Merging
* Removing Duplicates

---

## Core Idea

Use two indices (pointers) that move based on conditions.

```
left ---------------- right
```

The pointers may:

* Move toward each other
* Move in the same direction
* Move independently

---

## General Template

```python
left = 0
right = len(arr) - 1

while left < right:

    if condition:
        return answer

    elif need_left:
        left += 1

    else:
        right -= 1
```

---

## Common Problems

* Two Sum II
* Valid Palindrome
* Merge Sorted Arrays
* Remove Duplicates from Sorted Array
* Container With Most Water
* 3Sum

---

## Time Complexity

```
Time: O(n)

Space: O(1)
```

---

# Sliding Window Pattern

Sliding Window is a specialized form of Two Pointers.

Instead of comparing two separate positions, the pointers maintain a **window** over a contiguous section of an array or string.

```
[left ........ right]
```

---

## Used For

* Subarrays
* Substrings
* Consecutive Elements
* Contiguous Segments

---

# Recognition Keywords

If a problem contains words like:

* Longest
* Shortest
* Maximum
* Minimum
* Subarray
* Substring
* Contiguous
* Consecutive

Sliding Window is often the correct approach.

---

# Types of Sliding Window

## 1. Fixed Size Window

The window size never changes.

Example:

Maximum Sum Subarray of Size K

### Template

```python
window_sum = sum(nums[:k])
answer = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right]
    window_sum -= nums[right-k]
    answer = max(answer, window_sum)
```

### Complexity

```
Time: O(n)

Space: O(1)
```

---

## 2. Variable Size Window

The window grows and shrinks dynamically.

Example:

Longest Substring Without Repeating Characters

### Template

```python
left = 0

for right in range(len(arr)):

    add(arr[right])

    while invalid_window:
        remove(arr[left])
        left += 1

    update_answer()
```

### Complexity

```
Time: O(n)

Space: O(k)
```

---

# Universal Sliding Window Framework

```python
left = 0
answer = 0

for right in range(len(arr)):

    # Expand
    add(arr[right])

    # Shrink
    while invalid_window:
        remove(arr[left])
        left += 1

    # Update answer
    answer = max(answer, current_window)
```

---

# Popular Sliding Window Problems

## Fixed Window

* Maximum Sum Subarray of Size K
* Average of Subarrays of Size K
* Maximum Number of Vowels in a Substring

---

## Variable Window

* Longest Substring Without Repeating Characters
* Minimum Window Substring
* Longest Repeating Character Replacement
* Permutation in String
* Fruit Into Baskets
* Minimum Size Subarray Sum

---

# Two Pointers vs Sliding Window

| Two Pointers                 | Sliding Window               |
| ---------------------------- | ---------------------------- |
| General technique            | Specialized Two Pointers     |
| Mostly used on sorted arrays | Used for contiguous ranges   |
| Pointers move independently  | Pointers maintain one window |
| Pair problems                | Subarray/Substring problems  |

---

# Complexity Insight

Why is Sliding Window O(n)?

Each element:

* Enters the window once
* Leaves the window once

Total operations:

```
n + n = 2n

Time = O(n)
```

---

# Recognition Checklist

## Use Two Pointers When

* Sorted array
* Pair problems
* Palindrome
* Reverse array/string
* Merge arrays

---

## Use Sliding Window When

* Subarray
* Substring
* Contiguous elements
* Longest/Shortest
* Maximum/Minimum

---

# Interview Decision Tree

```
Array or String?

        │
        ▼

Contiguous Range?

        │
      Yes
        │
Sliding Window

        │
       No

Sorted Array?

        │
      Yes
        │
Two Pointers

        │
       No

Consider:
Hash Map
Stack
Queue
Binary Search
Graph
Tree
Dynamic Programming
```

---

# Quick Revision

## Two Pointers

* Sorted Arrays
* Palindrome
* Pair Problems
* Merge Arrays

Time: O(n)

Space: O(1)

---

## Sliding Window

Used For:

* Subarrays
* Substrings
* Consecutive Elements

Types:

1. Fixed Window
2. Variable Window

Pattern:

```
Expand
↓

Shrink if needed
↓

Update Answer
```

Benefits:

```
O(n²)
↓

O(n)
```

---

# Key Takeaways

✅ Recognize common interview patterns.

✅ Use Two Pointers for sorted arrays and pair-related problems.

✅ Use Sliding Window for contiguous subarrays and substrings.

✅ Most Sliding Window problems follow:

Expand → Shrink → Update Answer.

Mastering these patterns will solve many medium-level interview questions efficiently.