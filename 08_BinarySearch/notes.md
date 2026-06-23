# Binary Search

**Binary Search** is an efficient searching algorithm used to find an element in a **sorted list or array**.

## Steps

1. Set `left` to 0.
2. Set `right` to the last index of the array.
3. Find the middle index:

   ```python
   mid = (left + right) // 2
   ```
4. Compare the middle element with the target value.
5. If they are equal, the target is found.
6. If the target is greater than the middle element, search the right half.
7. If the target is smaller than the middle element, search the left half.
8. Repeat the process until the target is found or the search space becomes empty.

## Example

Array:

```
[2, 4, 6, 8, 10, 12, 14]
```

Target:

```
10
```

Process:

* Middle element = 8
* 10 > 8, search right half
* Middle element = 12
* 10 < 12, search left half
* Middle element = 10
* Target found

## Time Complexity

* Best Case: **O(1)**
* Average Case: **O(log n)**
* Worst Case: **O(log n)**

## Space Complexity

* Iterative Binary Search: **O(1)**
* Recursive Binary Search: **O(log n)**

## Applications

* Searching in sorted arrays
* Database indexing
* Dictionary and phonebook searches
* Finding boundaries in sorted data
* Competitive programming and algorithm optimization

## Key Points

* Binary Search works only on **sorted data**.
* It repeatedly divides the search space into two halves.
* It is much faster than linear search for large datasets.
* The search space is reduced by half in each step.

