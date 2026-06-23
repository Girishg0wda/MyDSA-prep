# Sorting Algorithms

Sorting is the process of arranging elements in a specific order (ascending or descending).

---

## Why Sorting?

Sorting helps in:

* Faster searching
* Duplicate detection
* Data organization
* Scheduling problems
* Interval problems
* Efficient data processing

---

# Types of Sorting Algorithms

## 1. Bubble Sort

Repeatedly compares adjacent elements and swaps them if they are in the wrong order.

### Example

```python
nums = [5, 3, 8, 2]

n = len(nums)

for i in range(n):
    for j in range(n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
```

### Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n²)      |
| Worst   | O(n²)      |

### Space Complexity

```text
O(1)
```

### Advantages

* Easy to understand
* In-place sorting

### Disadvantages

* Very slow for large datasets

---

## 2. Selection Sort

Finds the minimum element and places it at the correct position.

### Example

```python
nums = [5, 3, 8, 2]

n = len(nums)

for i in range(n):
    min_idx = i

    for j in range(i + 1, n):
        if nums[j] < nums[min_idx]:
            min_idx = j

    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print(nums)
```

### Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n²)      |
| Average | O(n²)      |
| Worst   | O(n²)      |

### Space Complexity

```text
O(1)
```

### Advantages

* Fewer swaps compared to Bubble Sort
* In-place sorting

### Disadvantages

* Always O(n²)

---

## 3. Insertion Sort

Builds the sorted array one element at a time.

### Example

```python
nums = [5, 3, 8, 2]

for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = key

print(nums)
```

### Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n²)      |
| Worst   | O(n²)      |

### Space Complexity

```text
O(1)
```

### Advantages

* Efficient for small datasets
* Works well on nearly sorted arrays

### Disadvantages

* Slow for large datasets

---

# Python Built-in Sorting

Python provides two sorting methods.

## sorted()

Returns a new sorted list.

```python
nums = [5, 2, 8, 1]

result = sorted(nums)

print(result)
```

Output:

```python
[1, 2, 5, 8]
```

---

## sort()

Sorts the original list.

```python
nums = [5, 2, 8, 1]

nums.sort()

print(nums)
```

Output:

```python
[1, 2, 5, 8]
```

---

## Reverse Sorting

```python
nums.sort(reverse=True)

print(nums)
```

Output:

```python
[8, 5, 2, 1]
```

---

# Timsort

Python uses **Timsort**, a hybrid of:

* Merge Sort
* Insertion Sort

### Complexity

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(n)       |
| Average | O(n log n) |
| Worst   | O(n log n) |

### Advantages

* Stable sorting
* Efficient for real-world data
* Handles partially sorted data very well

---

# Comparison Table

| Algorithm      | Best  | Average    | Worst      | Space |
| -------------- | ----- | ---------- | ---------- | ----- |
| Bubble Sort    | O(n)  | O(n²)      | O(n²)      | O(1)  |
| Selection Sort | O(n²) | O(n²)      | O(n²)      | O(1)  |
| Insertion Sort | O(n)  | O(n²)      | O(n²)      | O(1)  |
| Python Timsort | O(n)  | O(n log n) | O(n log n) | O(n)  |

---

# Stable vs Unstable Sorting

### Stable Sort

Maintains the relative order of equal elements.

Examples:

* Bubble Sort
* Insertion Sort
* Merge Sort
* Timsort

### Unstable Sort

May change the order of equal elements.

Examples:

* Selection Sort
* Heap Sort
* Quick Sort (typically)

---

# Key Interview Points

* Bubble Sort swaps adjacent elements.
* Selection Sort repeatedly selects the minimum element.
* Insertion Sort inserts elements into the correct position.
* Insertion Sort performs well on nearly sorted arrays.
* Python uses Timsort internally.
* `sort()` modifies the original list.
* `sorted()` returns a new sorted list.
* Timsort has O(n log n) average and worst-case complexity.

---

# Applications of Sorting

* Binary Search
* Duplicate Detection
* Database Query Optimization
* Scheduling Problems
* Interval Merging
* Ranking Systems
* Data Analysis
* Searching Algorithms

