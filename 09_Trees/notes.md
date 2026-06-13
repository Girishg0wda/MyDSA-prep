# Trees

A **tree** is a hierarchical data structure consisting of nodes connected by edges. It represents parent-child relationships.

## Terminology

* **Root**: The topmost node in the tree.
* **Parent**: A node that has one or more child nodes.
* **Child**: A node directly connected to a parent node.
* **Leaf**: A node with no children.

## Binary Tree

A **binary tree** is a tree in which each node has at most two children: a left child and a right child.

Example:

```
10
```

/  
5   15

## Tree Traversals

Tree traversal is the process of visiting all nodes in a tree.

### 1. Preorder Traversal (Root → Left → Right)

For the example tree:

* Output: 10, 5, 15

### 2. Inorder Traversal (Left → Root → Right)

For the example tree:

* Output: 5, 10, 15

### 3. Postorder Traversal (Left → Right → Root)

For the example tree:

* Output: 5, 15, 10

## Applications of Trees

* File Systems
* Search Engines
* Databases
* Binary Search Trees (BSTs)
* Expression Parsing
* Organizational Hierarchies

## Key Points

* Trees are non-linear data structures.
* They are used to represent hierarchical relationships.
* Binary trees are a common and important type of tree.
* Traversal techniques are essential for processing tree data.
