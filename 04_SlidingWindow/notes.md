# Sliding Window

**Sliding Window** is an algorithmic technique used to efficiently process **subarrays** and **substrings** by maintaining a window that moves through the data structure.

Instead of repeatedly recalculating values for overlapping ranges, the window is adjusted incrementally, improving performance.

## Benefits

* Avoids unnecessary nested loops.
* Reduces time complexity from **O(n²)** to **O(n)** in many problems.
* Efficient for problems involving contiguous elements.
* Easy to implement for fixed-size and variable-size windows.

## How It Works

A window is maintained using two pointers:

* **Start Pointer** → Beginning of the window
* **End Pointer** → End of the window

The window slides through the array or string while updating the required information.

## Example

Array:

```text
[1, 3, 2, 6, -1, 4, 1, 8]
```

Window Size = 3

Windows:

```text
[1, 3, 2]
   [3, 2, 6]
      [2, 6, -1]
         [6, -1, 4]
```

Instead of recalculating each window from scratch, remove the outgoing element and add the incoming element.

## Common Problems

* Maximum Sum Subarray
* Longest Substring Without Repeating Characters
* Average of Subarrays
* Fixed Window Size Problems
* Minimum Size Subarray Sum
* Maximum Consecutive Ones

## Types of Sliding Window

### 1. Fixed-Size Window

The window size remains constant.

Example:

* Maximum sum of a subarray of size `k`

### 2. Variable-Size Window

The window expands or shrinks based on a condition.

Example:

* Longest substring without repeating characters

## Time Complexity

* **O(n)**

Each element is typically visited at most once.

## Space Complexity

* **O(1)** (excluding input storage)

May become **O(k)** when additional data structures are used.

## Key Points

* Best suited for contiguous subarray and substring problems.
* Uses two pointers to maintain a moving window.
* Eliminates redundant computations.
* Commonly used in coding interviews and competitive programming.
* Often converts brute-force O(n²) solutions into O(n) solutions.

