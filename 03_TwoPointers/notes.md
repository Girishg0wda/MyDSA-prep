# Two Pointers

## What is the Two Pointers Technique?

The **Two Pointers** technique is an algorithmic approach that uses two indices (pointers) to traverse a data structure, typically an array or string.

The pointers may:

* Start from opposite ends and move toward each other.
* Start from the same end and move at different speeds.
* Move based on specific conditions.

## Example

Array:

```text
[1, 2, 3, 4, 5]
```

```python
left = 0
right = 4
```

Visualization:

```text
left            right
 ↓                ↓
[1, 2, 3, 4, 5]
```

The pointers move according to the problem requirements until they meet or cross.

## Why Use It?

Instead of using nested loops with **O(n²)** complexity, many problems can be solved in **O(n)** by intelligently moving two pointers.

Benefits:

* Faster execution
* Reduced time complexity
* Constant extra space
* Simple and efficient implementation

## Common Problems

* Pair Sum (Two Sum in a Sorted Array)
* Reverse String
* Palindrome Check
* Remove Duplicates from Sorted Array
* Container With Most Water
* Trapping Rain Water
* Merge Sorted Arrays

## How It Works

1. Initialize two pointers.
2. Compare values at the pointers.
3. Move one or both pointers based on a condition.
4. Continue until the pointers meet or the desired result is found.

## Example: Palindrome Check

String:

```text
MADAM
```

Compare:

* M with M
* A with A
* D with D

Since all matching characters are equal, the string is a palindrome.

## Time Complexity

* **O(n)**

Each element is typically processed at most once.

## Space Complexity

* **O(1)**

Only a few extra variables are required.

## Key Idea

Move pointers based on conditions until they meet, cross, or satisfy the problem's requirement.

## Key Points

* Commonly used with sorted arrays and strings.
* Reduces many O(n²) solutions to O(n).
* Uses constant extra memory.
* Frequently asked in coding interviews.
* Works best when pointer movement can eliminate unnecessary comparisons.

