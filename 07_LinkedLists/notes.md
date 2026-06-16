# Linked Lists

A **Linked List** is a linear data structure made up of a sequence of nodes connected through pointers.

## Node Structure

Each node contains:

* **Data**: Stores the value of the node.
* **Pointer (Next)**: Stores the address of the next node.

## Structure

Example:

```text
10 -> 20 -> 30 -> None
```

* `10` is the first node (Head).
* `20` and `30` are subsequent nodes.
* `None` indicates the end of the list.

## Advantages

* Dynamic size (can grow or shrink during execution).
* Efficient insertion and deletion operations.
* Does not require contiguous memory allocation.

## Disadvantages

* No direct indexing; elements must be accessed sequentially.
* Extra memory is required to store pointers.
* Searching is slower compared to arrays.

## Types of Linked Lists

### 1. Singly Linked List

Each node points to the next node.

```text
10 -> 20 -> 30 -> None
```

### 2. Doubly Linked List

Each node contains pointers to both the previous and next nodes.

```text
None <- 10 <-> 20 <-> 30 -> None
```

### 3. Circular Linked List

The last node points back to the first node.

```text
10 -> 20 -> 30
^           |
|___________|
```

## Time Complexity

| Operation              | Time Complexity |
| ---------------------- | --------------- |
| Access                 | O(n)            |
| Search                 | O(n)            |
| Insertion at Beginning | O(1)            |
| Insertion at End       | O(n)            |
| Deletion at Beginning  | O(1)            |
| Deletion at End        | O(n)            |

## Common Interview Problems

* Reverse Linked List
* Detect Cycle in a Linked List
* Find the Middle Node
* Merge Two Sorted Linked Lists
* Remove Nth Node from End
* Check if Linked List is Palindrome

## Key Points

* Linked Lists are dynamic data structures.
* Nodes are connected using pointers.
* Insertion and deletion are efficient.
* Random access is not possible.
* Widely used in stacks, queues, and graph implementations.
