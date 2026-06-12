# Binary Search

Binary Search is an efficient searching algorithm that works on a sorted list.

Steps:
1. Set `left` to 0.
2. Set `right` to the last index.
3. Find the middle index:
   ```python
   mid = (left + right) // 2
   ```
4. Compare the middle value with the target.
5. If equal, the target is found.
6. If the target is larger, search the right half.
7. If the target is smaller, search the left half.
8. Repeat until found or the search space is empty.

Time Complexity: O(log n)
Space Complexity: O(1)