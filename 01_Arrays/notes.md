# Arrays

## What is an Array?

An **Array** is a linear data structure that stores a collection of elements in contiguous memory locations.

Each element can be accessed using its index.

## Example

```text
[4, 7, 2, 9, 1]
```

Index positions:

```text
Index:  0  1  2  3  4
Array: [4, 7, 2, 9, 1]
```

* First element: `4` (index 0)
* Last element: `1` (index 4)

## Common Operations

| Operation | Complexity |
| --------- | ---------- |
| Access    | O(1)       |
| Search    | O(n)       |
| Insert    | O(n)       |
| Delete    | O(n)       |

### Access

```python
arr[2]
```

Output:

```text
2
```

### Search

Find a target element by traversing the array.

```python
target = 9
```

### Insert

Inserting an element may require shifting elements.

```text
[4, 7, 2, 9, 1]
Insert 5 at index 2
[4, 7, 5, 2, 9, 1]
```

### Delete

Deleting an element may require shifting elements.

```text
[4, 7, 2, 9, 1]
Delete 2
[4, 7, 9, 1]
```

## Key Learnings

* Traversing arrays using loops
* Finding minimum and maximum values
* Counting elements based on conditions
* Calculating sums and averages
* Updating elements using indices
* Searching for specific values

## Common Interview Problems

* Find Maximum and Minimum Element
* Second Largest Element
* Remove Duplicates
* Rotate Array
* Move Zeroes
* Kadane's Algorithm (Maximum Subarray Sum)
* Two Sum

## Advantages

* Fast random access using indices
* Simple and easy to implement
* Efficient memory usage

## Disadvantages

* Fixed size in some languages
* Insertion and deletion can be costly
* Requires contiguous memory

## Key Points

* Arrays store elements in contiguous memory.
* Elements are accessed using indices.
* Access operations are very fast: **O(1)**.
* Insertion and deletion generally take **O(n)** time.
* Arrays are one of the most fundamental data structures used in programming.
