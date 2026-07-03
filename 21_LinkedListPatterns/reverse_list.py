from create_list import create_list

head = create_list()

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