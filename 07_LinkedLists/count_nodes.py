class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first = Node(5)
second = Node(10)
third = Node(15)

first.next = second
second.next = third

count = 0
current = first

while current:
    count += 1
    current = current.next

print(count)