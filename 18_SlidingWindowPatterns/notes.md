# Sliding Window Interview Pattern

Sliding Window is used when dealing with:

```text
Subarrays
Substrings
Consecutive Elements
Contiguous Segments
```

Instead of checking every possible range (O(n²)), maintain a moving window and process each element at most a few times.

---

# Core Idea

```text
Expand Window
↓
Window Becomes Invalid
↓
Shrink Window
↓
Update Answer
```

Most Sliding Window problems follow this exact pattern.

---

# Recognition Pattern

Look for keywords:

```text
Longest
Shortest
Maximum
Minimum
Largest
Smallest
```

Combined with:

```text
Substring
Subarray
Contiguous
Consecutive
Window
```

These are strong indicators of Sliding Window.

---

# Types of Sliding Window

## 1. Fixed Size Window

Window size is known.

Example:

```text
Maximum Sum Subarray of Size K
```

### Template

```python
window_sum = 0

for i in range(k):
    window_sum += nums[i]

answer = window_sum

for right in range(k, len(nums)):

    window_sum += nums[right]
    window_sum -= nums[right - k]

    answer = max(answer, window_sum)
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

## 2. Variable Size Window

Window grows and shrinks dynamically.

Example:

```text
Longest Substring Without Repeating Characters
```

### Template

```python
left = 0

for right in range(len(nums)):

    add(nums[right])

    while invalid_window:

        remove(nums[left])
        left += 1

    update_answer()
```

### Complexity

```text
Time: O(n)
Space: O(k)
```

---

# General Sliding Window Framework

```python
left = 0
answer = 0

for right in range(len(arr)):

    # Expand window
    add(arr[right])

    # Shrink if needed
    while invalid_window:

        remove(arr[left])
        left += 1

    # Update answer
    answer = max(answer, current_window)
```

---

# Problem 1: Maximum Sum Subarray of Size K

Goal:

```text
Find maximum sum among all
subarrays of size K.
```

Example:

```text
nums = [2,1,5,1,3,2]
k = 3
```

Window Sums:

```text
2+1+5 = 8
1+5+1 = 7
5+1+3 = 9
1+3+2 = 6
```

Answer:

```text
9
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# Problem 2: Longest Substring Without Repeating Characters

Goal:

```text
Find longest substring
containing unique characters.
```

Example:

```text
"abcabcbb"
```

Answer:

```text
3
```

Substring:

```text
"abc"
```

### Solution

```python
left = 0
seen = set()
answer = 0

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    answer = max(
        answer,
        right - left + 1
    )
```

### Complexity

```text
Time: O(n)
Space: O(k)
```

---

# Problem 3: Minimum Window Substring

Goal:

```text
Find smallest substring
containing all required characters.
```

Example:

```text
s = "ADOBECODEBANC"
t = "ABC"
```

Answer:

```text
"BANC"
```

### Pattern

```text
Expand until valid
↓
Shrink while valid
↓
Track minimum length
```

### Complexity

```text
Time: O(n)
Space: O(k)
```

---

# Problem 4: Longest Repeating Character Replacement

Goal:

```text
Replace at most k characters
to make longest repeating substring.
```

Example:

```text
s = "AABABBA"
k = 1
```

Answer:

```text
4
```

### Key Formula

```python
window_size - max_frequency <= k
```

Valid window:

```text
Characters needing replacement
must not exceed k
```

### Complexity

```text
Time: O(n)
Space: O(1)
```

---

# Common Sliding Window Questions

## Fixed Window

```text
Maximum Sum Subarray Size K
Average of Subarrays Size K
Maximum Number of Vowels
```

---

## Variable Window

```text
Longest Substring Without Repeating Characters
Minimum Window Substring
Longest Repeating Character Replacement
Permutation in String
Fruit Into Baskets
```

---

# Sliding Window vs Two Pointers

Sliding Window is a specialized form of Two Pointers.

Two Pointers:

```text
Pointers move based on conditions.
```

Sliding Window:

```text
Pointers define a window
representing a contiguous range.
```

Example:

```text
left -------- right
```

Window:

```text
[left ... right]
```

---

# Complexity Insight

Why O(n)?

```text
Each element enters
the window once.

Each element leaves
the window once.
```

Therefore:

```text
Total operations ≤ 2n
```

So:

```text
Time: O(n)
```

---

# Recognition Checklist

Use Sliding Window when:

✅ Array or String

✅ Contiguous elements

✅ Subarray / Substring

✅ Longest / Shortest / Maximum / Minimum

✅ Window can expand and shrink

Keywords:

```text
Substring
Subarray
Consecutive
Contiguous
Window
Longest
Shortest
Maximum
Minimum
```

---

# Interview Formula

```text
Contiguous Range
        ↓
Use Window
        ↓
Expand Right
        ↓
Shrink Left If Invalid
        ↓
Update Answer
        ↓
O(n) Solution
```

---

# Quick Revision

```text
Sliding Window

Used For:
- Subarrays
- Substrings
- Consecutive Elements

Types:
1. Fixed Window
2. Variable Window

Template:
Expand
Shrink
Update Answer

Benefits:
O(n²) → O(n)

Most Asked:
- Maximum Sum Subarray
- Longest Unique Substring
- Minimum Window Substring
- Character Replacement
- Permutation in String
```
