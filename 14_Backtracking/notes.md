# Backtracking

Backtracking is a recursive problem-solving technique used to explore all possible solutions by building a solution step by step and removing choices that do not lead to a valid solution.

---

# Core Idea

Backtracking follows three steps:

1. **Choose** → Make a decision.
2. **Explore** → Recurse with the current choice.
3. **Undo (Backtrack)** → Remove the choice and try another option.

---

# General Template

```python
def backtrack(path, choices):

    if goal_reached(path):
        result.append(path[:])
        return

    for choice in choices:

        # Choose
        path.append(choice)

        # Explore
        backtrack(path, choices)

        # Undo
        path.pop()
```

---

# Visual Example

Generate all subsets of:

```python
[1, 2]
```

Decision Tree:

```text
                []
              /    \
            1       skip
          /   \
       [1]    []
      /  \    /  \
   [1,2] [1] [2] []
```

Result:

```python
[
 [],
 [1],
 [2],
 [1,2]
]
```

---

# Example 1: Subsets

```python
def subsets(nums):

    result = []
    path = []

    def backtrack(index):

        result.append(path[:])

        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)

    return result
```

### Complexity

```text
Time: O(2^n)
Space: O(n)
```

---

# Example 2: Permutations

```python
def permute(nums):

    result = []

    def backtrack(path):

        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in nums:

            if num in path:
                continue

            path.append(num)
            backtrack(path)
            path.pop()

    backtrack([])

    return result
```

### Complexity

```text
Time: O(n!)
Space: O(n)
```

---

# Example 3: Combination Sum

```python
def combinationSum(candidates, target):

    result = []

    def backtrack(start, path, total):

        if total == target:
            result.append(path[:])
            return

        if total > target:
            return

        for i in range(start, len(candidates)):

            path.append(candidates[i])

            backtrack(
                i,
                path,
                total + candidates[i]
            )

            path.pop()

    backtrack(0, [], 0)

    return result
```

---

# Example 4: N Queens

Place N queens on an N×N chessboard such that:

- No two queens share a row
- No two queens share a column
- No two queens share a diagonal

Backtracking tries every valid queen placement and removes invalid choices.

### Complexity

```text
Time: O(N!)
Space: O(N)
```

---

# Example 5: Sudoku Solver

Fill empty cells while satisfying Sudoku rules:

- Each row contains 1-9
- Each column contains 1-9
- Each 3×3 box contains 1-9

Backtracking:

1. Find empty cell
2. Try digits 1-9
3. Recurse
4. Undo if invalid

### Complexity

```text
Exponential
```

---

# Common Backtracking Problems

## Easy

- Subsets
- Subsets II
- Letter Combinations of Phone Number

## Medium

- Permutations
- Permutations II
- Combination Sum
- Combination Sum II
- Palindrome Partitioning
- Word Search

## Hard

- N Queens
- Sudoku Solver
- Rat in a Maze
- Crossword Solver

---

# Backtracking vs DFS

| Feature | DFS | Backtracking |
|----------|----------|----------|
| Traversal | Yes | Yes |
| Undo Choices | No | Yes |
| Generate Solutions | Limited | Excellent |
| Search Space Exploration | Basic | Complete |

Backtracking is essentially DFS + Undoing Decisions.

---

# Key Operations

### Add Choice

```python
path.append(x)
```

### Remove Choice

```python
path.pop()
```

The `pop()` operation is the heart of backtracking.

---

# Complexity

Backtracking usually explores many possibilities.

| Problem | Complexity |
|----------|------------|
| Subsets | O(2^n) |
| Permutations | O(n!) |
| N Queens | O(N!) |
| Sudoku | Exponential |

---

# Recognition Pattern

Use Backtracking when:

✅ Need all possible solutions

✅ Need all combinations

✅ Need all permutations

✅ Need to explore every path

✅ Problem involves choices and constraints

Common keywords:

- Generate all
- Find all combinations
- Find all permutations
- Explore every path
- Valid arrangement

---

# Interview Tips

1. Backtracking = Choose → Explore → Undo.
2. `path.pop()` performs the undo operation.
3. Backtracking is recursive.
4. Used for combinations, permutations, subsets, and constraint problems.
5. Often implemented using DFS.
6. Time complexity is usually exponential.
7. Pruning invalid paths improves performance.

---

# Quick Revision

```text
Choose
↓
Explore
↓
Undo
```

Core Template:

```python
path.append(choice)

backtrack(...)

path.pop()
```

Remember:

Backtracking = DFS + Undoing Decisions