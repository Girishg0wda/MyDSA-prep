class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list():
    first = Node(5)
    second = Node(10)
    third = Node(15)

    first.next = second
    second.next = third

    return first


if __name__ == "__main__":
    first = create_linked_list()

    # Print the list
    current = first

    while current:
        print(current.data)
        current = current.next

    # Search for a value
    target = 10

    current = first
    found = False

    while current:
        if current.data == target:
            found = True
            break

        current = current.next

    print(found)