# Dynamic Programming (DP)

Dynamic Programming (DP) is an optimization technique used to solve problems by breaking them into smaller overlapping subproblems and storing previously computed results.

---

# Core Idea

DP works when a problem has:

### 1. Overlapping Subproblems

The same subproblem is solved multiple times.

Example:

```python
fib(5)
├── fib(4)
│   ├── fib(3)
│   └── fib(2)
└── fib(3)
```

`fib(3)` is computed repeatedly.

---

### 2. Optimal Substructure

The optimal solution can be built from optimal solutions of smaller subproblems.

Example:

```python
fib(n) = fib(n-1) + fib(n-2)
```

---

# Two Approaches

## 1. Memoization (Top-Down)

Use recursion + cache.

```python
memo = {}

def dp(n):

    if n in memo:
        return memo[n]

    memo[n] = dp(n-1) + dp(n-2)

    return memo[n]
```

### Characteristics

* Recursive
* Easy to write
* Computes only needed states

---

## 2. Tabulation (Bottom-Up)

Build answers from smallest subproblems.

```python
def fib(n):

    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

### Characteristics

* Iterative
* No recursion stack
* Usually faster

---

# DP Problem Solving Framework

Whenever you see a DP problem:

### Step 1: Define State

Ask:

```text
What information uniquely describes a subproblem?
```

Example:

```python
dp[i]
```

Meaning:

```text
Answer for first i elements
```

---

### Step 2: Find Recurrence Relation

Ask:

```text
How can I build current answer from previous answers?
```

Example:

```python
dp[i] = dp[i-1] + dp[i-2]
```

---

### Step 3: Identify Base Cases

Example:

```python
dp[0] = 0
dp[1] = 1
```

---

### Step 4: Compute Answer

Memoization:

```python
return dp(n)
```

Tabulation:

```python
return dp[n]
```

---

# Example 1: Fibonacci

## Recursive

```python
def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)
```

### Complexity

```text
Time: O(2^n)
Space: O(n)
```

---

## DP

```python
def fib(n):

    if n <= 1:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# Example 2: Climbing Stairs

Problem:

```text
You can climb either 1 or 2 steps.
How many distinct ways to reach n?
```

Recurrence:

```python
dp[i] = dp[i-1] + dp[i-2]
```

Solution:

```python
def climbStairs(n):

    if n <= 2:
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# Example 3: House Robber

Problem:

```text
Cannot rob adjacent houses.
Maximize money stolen.
```

State:

```python
dp[i]
```

Meaning:

```text
Maximum money from first i houses.
```

Recurrence:

```python
dp[i] = max(
    dp[i-1],
    dp[i-2] + nums[i]
)
```

### Complexity

```text
Time: O(n)
Space: O(n)
```

---

# Example 4: Coin Change

Problem:

```text
Minimum coins needed to make amount.
```

State:

```python
dp[a]
```

Meaning:

```text
Minimum coins to form amount a.
```

Recurrence:

```python
dp[a] = min(
    dp[a],
    dp[a - coin] + 1
)
```

### Complexity

```text
Time: O(amount × coins)
Space: O(amount)
```

---

# Example 5: Longest Common Subsequence (LCS)

Problem:

```text
Find longest common subsequence
between two strings.
```

State:

```python
dp[i][j]
```

Meaning:

```text
LCS length of
text1[:i]
text2[:j]
```

Recurrence:

```python
if text1[i-1] == text2[j-1]:
    dp[i][j] = 1 + dp[i-1][j-1]
else:
    dp[i][j] = max(
        dp[i-1][j],
        dp[i][j-1]
    )
```

### Complexity

```text
Time: O(m × n)
Space: O(m × n)
```

---

# DP State Patterns

## 1D DP

```python
dp[i]
```

Examples:

* Fibonacci
* Climbing Stairs
* House Robber
* Coin Change

---

## 2D DP

```python
dp[i][j]
```

Examples:

* LCS
* Edit Distance
* Unique Paths

---

## String DP

Examples:

* LCS
* Palindrome Partitioning
* Edit Distance

---

## Grid DP

Examples:

* Unique Paths
* Minimum Path Sum

---

## Knapsack DP

Examples:

* 0/1 Knapsack
* Partition Equal Subset Sum
* Target Sum

---

# Space Optimization

Many DP problems only use previous states.

Example:

```python
dp[i] = dp[i-1] + dp[i-2]
```

Instead of:

```python
dp = [0] * n
```

Use:

```python
prev2 = 0
prev1 = 1

for i in range(2, n+1):

    curr = prev1 + prev2

    prev2 = prev1
    prev1 = curr
```

Space becomes:

```text
O(1)
```

---

# Common DP Problems

## Easy

* Fibonacci Number
* Climbing Stairs
* Min Cost Climbing Stairs

---

## Medium

* House Robber
* Coin Change
* Unique Paths
* Partition Equal Subset Sum
* Longest Increasing Subsequence

---

## Hard

* Edit Distance
* Burst Balloons
* Regular Expression Matching
* Distinct Subsequences
* Palindrome Partitioning II

---

# Backtracking vs DP

| Feature         | Backtracking            | DP                    |
| --------------- | ----------------------- | --------------------- |
| Goal            | Generate solutions      | Optimize solutions    |
| Stores Results  | No                      | Yes                   |
| Repeated Work   | Yes                     | Avoided               |
| Time Complexity | Usually Exponential     | Usually Polynomial    |
| Technique       | Choose → Explore → Undo | Solve → Store → Reuse |

---

# Recognition Pattern

Use DP when:

✅ Repeated subproblems exist

✅ Need minimum/maximum answer

✅ Need count of ways

✅ Need optimal solution

✅ Problem asks for longest/shortest/best

Common keywords:

* Minimum
* Maximum
* Count Ways
* Longest
* Shortest
* Optimal
* Best

---

# Interview Tips

1. DP = Recursion + Caching.
2. Define state clearly.
3. Write recurrence relation.
4. Handle base cases.
5. Convert recursion to tabulation if needed.
6. Optimize space when possible.
7. Most DP questions reduce to a recurrence.

---

# Master DP Formula

```text
State
↓
Recurrence
↓
Base Case
↓
Memoization / Tabulation
↓
Answer
```

---

# Quick Revision

```text
DP = Store Previous Results

Requirements:
1. Overlapping Subproblems
2. Optimal Substructure

Approaches:
- Memoization (Top Down)
- Tabulation (Bottom Up)

Common Keywords:
- Minimum
- Maximum
- Count Ways
- Longest
- Optimal
```
