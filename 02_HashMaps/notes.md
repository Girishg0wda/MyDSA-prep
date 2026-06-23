# Hash Maps

## What is a Hash Map?

A **Hash Map** (also called a **Hash Table** or **Dictionary**) is a data structure that stores data in **key-value pairs**.

Each key is unique and is used to quickly access its corresponding value.

## Example

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
```

* Key: `"name"` → Value: `"John"`
* Key: `"age"` → Value: `20`
* Key: `"grade"` → Value: `"A"`

## Why Use Hash Maps?

Hash Maps provide very fast insertion, deletion, and lookup operations.

Instead of searching through all elements, a hash function computes an index where the data is stored.

## Common Operations

### Insert

```python
hash_map["city"] = "Mysore"
```

### Access

```python
hash_map["city"]
```

### Update

```python
hash_map["city"] = "Bangalore"
```

### Delete

```python
del hash_map["city"]
```

### Check Existence

```python
"city" in hash_map
```

## Common Problems

* Two Sum
* Frequency Counting
* Duplicate Detection
* Group Anagrams
* Longest Consecutive Sequence
* First Non-Repeating Character

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Insert    | O(1)       |
| Search    | O(1)       |
| Delete    | O(1)       |

### Worst Case

| Operation | Complexity |
| --------- | ---------- |
| Insert    | O(n)       |
| Search    | O(n)       |
| Delete    | O(n)       |

Worst-case occurs due to hash collisions.

## Space Complexity

* **O(n)**

Where `n` is the number of key-value pairs stored.

## Advantages

* Fast lookup and updates
* Efficient key-value storage
* Average O(1) operations
* Easy frequency counting

## Disadvantages

* Uses extra memory
* Performance may decrease because of collisions
* Keys must be hashable

## Key Idea

Use a **key** to directly access a **value** without scanning the entire data structure.

## Key Points

* Stores data as key-value pairs.
* Keys are unique.
* Average insertion, search, and deletion take O(1) time.
* One of the most important data structures for coding interviews.
* Frequently used for counting, caching, and fast lookups.
