class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(5)
second = Node(10)
third = Node(15)

first.next = second
second.next = third

print(first.data)
print(first.next.data)
print(first.next.next.data)
