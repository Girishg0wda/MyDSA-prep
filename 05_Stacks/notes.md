# Stacks

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

This means the last element inserted into the stack is the first element removed.

## LIFO Principle

**LIFO = Last In, First Out**

Example:

```text
Top
 |
30
20
10
```

* 30 was inserted last, so it is removed first.
* 10 was inserted first, so it is removed last.

## Operations

### Push

Adds an element to the top of the stack.

```python
stack.append(x)
```

### Pop

Removes and returns the top element from the stack.

```python
stack.pop()
```

### Peek (Top)

Returns the top element without removing it.

```python
stack[-1]
```

## Example

```text
Initial Stack:
Top
 |
20
10

Push(30):
Top
 |
30
20
10

Pop():
Top
 |
20
10
```

## Applications

* Browser Back Button
* Undo/Redo Feature
* Expression Evaluation
* Valid Parentheses Checking
* Function Call Management (Call Stack)
* Depth-First Search (DFS)

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | O(1)       |
| Pop       | O(1)       |
| Peek      | O(1)       |

## Python Implementation

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

stack.pop()
```

## Key Points

* Stack follows the LIFO principle.
* Insertion and deletion occur only at the top.
* Python lists can be used to implement stacks efficiently.
* Stacks are widely used in recursion, expression evaluation, and backtracking algorithms.
