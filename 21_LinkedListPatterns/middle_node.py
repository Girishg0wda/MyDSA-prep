class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

print(slow.data)