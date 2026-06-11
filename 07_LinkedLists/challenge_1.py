# Challenge 2
# Count the nodes in:
# 5 → 10 → 15 → None
# Expected:
# 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(5)
second = Node(10)
third = Node(15)

first.next = second
second.next = third

current = first

while current:
    print(current.data)
    current = current.next