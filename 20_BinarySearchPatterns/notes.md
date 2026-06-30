# Day 20 – Interview Pattern (Hash Maps & Sets)

## Overview

Today focuses on one of the most important interview patterns:

* Hash Maps (Dictionary)
* Hash Sets

These data structures allow **constant-time lookups**, making many brute-force **O(n²)** solutions become **O(n)**.

---

# Hash Map Pattern

## Used For

* Fast lookup
* Frequency counting
* Storing key-value pairs
* Tracking visited elements
* Index mapping

---

## Core Idea

Store useful information while traversing the array or string.

```
Value  → Information

Number → Index
Character → Frequency
Prefix Sum → Count
```

---

## Python Data Structures

### Dictionary

```python
mp = {}

mp["apple"] = 2
mp["banana"] = 5

print(mp["apple"])
```

---

### Hash Set

```python
seen = set()

seen.add(5)
seen.add(10)

print(5 in seen)
```

---

# Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Insert    | O(1)       |
| Search    | O(1)       |
| Delete    | O(1)       |

Average case complexity.

---

# Frequency Counting

One of the most common interview techniques.

Example:

```python
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

Result:

```
[1,2,2,3,3,3]

↓

{
1:1,
2:2,
3:3
}
```

---

# Using collections.Counter

```python
from collections import Counter

freq = Counter(nums)
```

Example:

```python
Counter([1,2,2,3])

↓

{
2:2,
1:1,
3:1
}
```

---

# Two Sum Pattern

Classic Hash Map problem.

Brute Force

```
O(n²)
```

Optimal

```
O(n)
```

Template

```python
mp = {}

for i, num in enumerate(nums):

    diff = target - num

    if diff in mp:
        return [mp[diff], i]

    mp[num] = i
```

---

# Duplicate Detection

Instead of nested loops:

```python
seen = set()

for num in nums:

    if num in seen:
        return True

    seen.add(num)

return False
```

Complexity

```
Time: O(n)

Space: O(n)
```

---

# Counting Frequencies

Example:

Top K Frequent Elements

```python
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

Used in:

* Top K Frequent Elements
* Majority Element
* Sort Characters by Frequency

---

# Grouping Pattern

Useful for anagrams.

```python
groups = {}

for word in strs:

    key = "".join(sorted(word))

    groups.setdefault(key, []).append(word)

return list(groups.values())
```

---

# Prefix Sum + Hash Map

Useful for subarray problems.

Template

```python
mp = {0:1}

prefix = 0

for num in nums:

    prefix += num

    if prefix - k in mp:
        answer += mp[prefix-k]

    mp[prefix] = mp.get(prefix,0)+1
```

Used in:

* Subarray Sum Equals K
* Continuous Subarray Sum

---

# Common Hash Map Problems

Easy

* Two Sum
* Contains Duplicate
* Valid Anagram
* Intersection of Two Arrays

Medium

* Group Anagrams
* Top K Frequent Elements
* Longest Consecutive Sequence
* Subarray Sum Equals K

Hard

* Minimum Window Substring
* Alien Dictionary
* LFU Cache

---

# Hash Set Pattern

Used For

* Duplicate checking
* Membership testing
* Visited nodes
* Unique values

Example

```python
seen = set()

for x in nums:

    if x in seen:
        return True

    seen.add(x)
```

---

# Recognition Checklist

Use Hash Map When

* Need fast lookup
* Frequency counting
* Store indices
* Pair lookup
* Prefix sums
* Group similar items

---

Use Hash Set When

* Need uniqueness
* Need duplicate detection
* Membership testing
* Visited tracking

---

# Decision Tree

```
Need Fast Lookup?

        │
      Yes
        │
Need Value → Info?

        │
      Yes
        │
Hash Map

        │
Need Only Presence?

        │
      Yes
        │
Hash Set
```

---

# Complexity Summary

| Data Structure | Search | Insert | Delete |
| -------------- | ------ | ------ | ------ |
| Hash Map       | O(1)   | O(1)   | O(1)   |
| Hash Set       | O(1)   | O(1)   | O(1)   |

Average-case complexities.

---

# Universal Templates

## Frequency Count

```python
freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

---

## Lookup While Traversing

```python
mp = {}

for i, num in enumerate(nums):

    if condition:
        return answer

    mp[num] = i
```

---

## Hash Set

```python
seen = set()

for x in arr:

    if x in seen:
        return True

    seen.add(x)
```

---

# Interview Tips

* Ask yourself if repeated searching can be replaced by a Hash Map.
* Use a Hash Set when only uniqueness or existence matters.
* Use `.get(key, default)` to avoid `KeyError`.
* Remember that Python dictionaries preserve insertion order (Python 3.7+), but interview questions usually rely only on average **O(1)** operations.

---

# Quick Revision

## Hash Map

Used For:

* Fast lookup
* Frequency counting
* Index storage
* Prefix sums
* Grouping

Time:

```
Search : O(1)
Insert : O(1)
Delete : O(1)
```

---

## Hash Set

Used For:

* Duplicate detection
* Membership testing
* Visited tracking

Time:

```
Search : O(1)
Insert : O(1)
Delete : O(1)
```

---

# Key Takeaways

✅ Hash Maps replace repeated searches with constant-time lookups.

✅ Hash Sets are ideal when only uniqueness or existence matters.

✅ Frequency counting is one of the most common interview techniques.

✅ Many array and string problems improve from **O(n²)** to **O(n)** using Hash Maps or Sets.

Mastering Hash Maps and Sets will help solve a large class of coding interview problems efficiently.

remove tomorrow