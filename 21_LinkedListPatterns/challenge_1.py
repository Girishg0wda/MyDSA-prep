# Challenge 1
# Reverse:
# 10 → 20 → 30 → None
# Expected:
# 30
# 20
# 10


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)

prev = None
current = head

while current:
    nxt = current.next
    current.next = prev
    prev = current
    current = nxt

head = prev

current = head

while current:
    print(current.data)
    current = current.next