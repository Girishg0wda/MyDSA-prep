from create_list import create_list

head = create_list()

current = head

while current:
    print(current.data)
    current = current.next