# Day 21 – Interview Pattern (Binary Search)

## Overview

Binary Search is one of the most important coding interview patterns.

Many candidates know the basic algorithm but fail to recognize when to use it.

The key interview skill is identifying **monotonic problems**, where the answer space can be divided into two parts:

- One part where the condition is **False**
- One part where the condition is **True**

Binary Search helps reduce search time from **O(n)** to **O(log n)**.

---

# When Should You Think of Binary Search?

Use Binary Search when you see phrases like:

- Sorted array
- Sorted list
- Search efficiently
- Find first occurrence
- Find last occurrence
- Minimum value satisfying a condition
- Maximum value satisfying a condition
- Closest value
- Search in answer space

---

# Mental Model

Imagine searching for a word in a dictionary.

You don't start from page 1.

You:

- Open the middle page.
- Decide whether to go left or right.
- Repeat.

Each step cuts the search space in half.

```
1000 Elements

↓

500

↓

250

↓

125

↓

63

↓

31

↓

16

↓

8

↓

4

↓

2

↓

1
```

This is why Binary Search runs in **O(log n)** time.

---

# Requirements

Binary Search usually requires:

- Sorted data
- Monotonic condition

Without one of these, Binary Search usually cannot be applied.

---

# Binary Search Algorithm

1. Find the middle element.
2. Compare with target.
3. If target is smaller, move left.
4. If target is larger, move right.
5. Repeat until found or search space is empty.

---

# Basic Binary Search Template

```python
def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

---

# Complexity

Time

```
O(log n)
```

Space

```
O(1)
```

---

# Example

```
Array

[2,4,6,8,10,12,14]

Target = 10

Middle = 8

Target > 8

↓

Search Right Half

Middle = 12

Target < 12

↓

Search Left Half

Middle = 10

Found
```

---

# First Occurrence

Sometimes duplicates exist.

Example

```
[1,2,2,2,3]
```

Need the **first** occurrence.

Template

```python
def first_occurrence(nums, target):

    left = 0
    right = len(nums) - 1
    answer = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            answer = mid
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer
```

---

# Last Occurrence

```python
def last_occurrence(nums, target):

    left = 0
    right = len(nums)-1
    answer = -1

    while left <= right:

        mid = (left + right)//2

        if nums[mid] == target:
            answer = mid
            left = mid + 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return answer
```

---

# Lower Bound

Find the first element **greater than or equal to** target.

Example

```
Array

[1,3,5,7,9]

Target = 6

Answer = Index of 7
```

---

# Upper Bound

Find the first element **greater than** target.

Example

```
Array

[1,3,5,5,5,7]

Target = 5

Answer = Index of 7
```

---

# Binary Search on Answer

Many interview problems do **not** ask you to search an array.

Instead, search the **possible answers**.

Example

```
Minimum Speed to Eat Bananas

Can Koko eat at speed = 5?

Yes

↓

Try smaller speed.

No?

↓

Try larger speed.
```

This pattern is called **Binary Search on Answer**.

---

# Recognition Checklist

Think Binary Search if:

- Array is sorted
- Need minimum possible answer
- Need maximum possible answer
- Search space can be divided
- Condition changes only once
- Looking for boundary
- Logarithmic solution expected

---

# Monotonic Condition

A condition is monotonic if it changes only once.

Example

```
Speed

1 2 3 4 5 6 7

False False False True True True True
```

Perfect for Binary Search.

---

# Common Binary Search Problems

## Easy

- Binary Search
- Search Insert Position
- Guess Number Higher or Lower
- Valid Perfect Square

---

## Medium

- Find First and Last Position
- Search in Rotated Sorted Array
- Find Peak Element
- Koko Eating Bananas
- Capacity To Ship Packages
- Search a 2D Matrix

---

## Hard

- Median of Two Sorted Arrays
- Split Array Largest Sum
- Aggressive Cows
- Allocate Minimum Pages

---

# Universal Templates

## Standard Binary Search

```python
left = 0
right = len(nums)-1

while left <= right:

    mid = (left + right)//2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1
```

---

## Binary Search on Answer

```python
left = minimum_possible
right = maximum_possible

while left <= right:

    mid = (left + right)//2

    if can_do(mid):

        answer = mid
        right = mid - 1

    else:
        left = mid + 1
```

---

# Time Complexity

| Operation | Complexity |
| ---------- | ---------- |
| Search | O(log n) |
| Space | O(1) |

---

# Common Mistakes

## Mistake 1

Wrong loop condition.

Wrong

```python
while left < right:
```

Sometimes this misses the last element.

Correct

```python
while left <= right:
```

---

## Mistake 2

Infinite loop.

Wrong

```python
left = mid
```

Correct

```python
left = mid + 1
```

---

## Mistake 3

Overflow in some languages.

Instead of

```python
mid = (left + right)//2
```

Use

```python
mid = left + (right-left)//2
```

Python doesn't overflow, but Java/C++ can.

---

## Mistake 4

Applying Binary Search on an unsorted array.

Binary Search requires:

- Sorted array
OR
- Monotonic answer space

---

# Debugging Tips

If your Binary Search isn't working:

1. Print `left`, `right`, and `mid` each iteration.
2. Verify the array is sorted.
3. Ensure `left` and `right` are updated correctly.
4. Check whether you're searching for:
   - Exact value
   - First occurrence
   - Last occurrence
   - Lower bound
   - Upper bound
5. Watch for infinite loops caused by incorrect pointer updates.

---

# Decision Tree

```
Need to search?

        │
       Yes
        │
Is data sorted?

        │
       Yes
        │
Binary Search

        │
Need minimum/maximum valid answer?

        │
       Yes
        │
Binary Search on Answer
```

---

# Interview Tips

- Always ask if the data is sorted.
- If not sorted, ask whether the **answer space** is monotonic.
- Learn the standard Binary Search template by heart.
- Practice first occurrence, last occurrence, lower bound, and upper bound.
- Many optimization problems use Binary Search on Answer.

---

# Quick Revision

## Binary Search

Used For

- Sorted arrays
- Fast searching
- Finding boundaries
- Optimization problems
- Binary Search on Answer

Time

```
Search : O(log n)
```

Space

```
O(1)
```

---

# Key Takeaways

✅ Binary Search reduces search time from **O(n)** to **O(log n)**.

✅ It works on **sorted data** or **monotonic answer spaces**.

✅ Learn the standard template before advanced variations.

✅ Binary Search on Answer is one of the most common interview patterns.

✅ Always recognize problems involving minimum or maximum feasible values.

Mastering Binary Search will prepare you for many array, optimization, and search problems commonly asked in coding interviews.