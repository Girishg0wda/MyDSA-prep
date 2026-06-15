# Recursion

Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.

## Structure of Recursion

Every recursive function has:

### 1. Base Case

The condition that stops the recursion.

```text
if n == 0:
    return
```

### 2. Recursive Case

The function calls itself with a smaller subproblem.

```text
return n + sum(n - 1)
```

---

## How Recursion Works

When a function calls itself, each call is stored in the **call stack** until the base case is reached.

Example:

```text
factorial(3)
```

Call Stack:

```text
factorial(3)
factorial(2)
factorial(1)
factorial(0)
```

Returning:

```text
1
1 × 1 = 1
2 × 1 = 2
3 × 2 = 6
```

---

## Example: Factorial

Factorial of a number:

```text
n! = n × (n-1) × (n-2) × ... × 1
```

Recursive definition:

```text
factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

Example:

```text
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= ...
= 120
```

### Complexity

| Metric | Complexity |
| ------ | ---------- |
| Time   | O(n)       |
| Space  | O(n)       |

---

## Example: Fibonacci

```text
fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)
```

Sequence:

```text
0, 1, 1, 2, 3, 5, 8, 13...
```

### Complexity

| Method           | Complexity |
| ---------------- | ---------- |
| Simple Recursion | O(2ⁿ)      |
| Memoization / DP | O(n)       |

---

## Applications of Recursion

* Tree Traversals
* Graph DFS
* Backtracking
* Dynamic Programming
* Binary Search
* Merge Sort
* Quick Sort
* Recursive Sum
* Factorial and Fibonacci Problems

---

## Advantages

* Simple and elegant code
* Natural solution for trees and graphs
* Useful for divide-and-conquer algorithms

---

## Disadvantages

* Uses extra memory (call stack)
* Can be slower than iterative solutions
* Risk of stack overflow for deep recursion

---

## Recursion vs Iteration

| Feature         | Recursion                 | Iteration                  |
| --------------- | ------------------------- | -------------------------- |
| Uses Call Stack | Yes                       | No                         |
| Memory Usage    | Higher                    | Lower                      |
| Readability     | Cleaner for some problems | Often more straightforward |
| Performance     | Can be slower             | Usually faster             |

---

## Key Points

* Recursion is when a function calls itself.
* Every recursive function must have:

  * Base Case
  * Recursive Case
* Recursive calls are stored in the call stack.
* Recursion is commonly used in trees, graphs, and backtracking.
* Deep recursion may cause stack overflow.
