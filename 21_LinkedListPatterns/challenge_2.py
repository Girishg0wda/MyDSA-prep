# Challenge 2
# Find the middle node of:
# 5 → 10 → 15 → 20 → 25
# Expected:
# 15

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


head = ListNode(5)
head.next = ListNode(10)
head.next.next = ListNode(15)
head.next.next.next = ListNode(20)
head.next.next.next.next = ListNode(25)

slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print(slow.data)