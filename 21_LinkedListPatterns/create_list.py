class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_list():
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)

    first.next = second
    second.next = third

    return first


if __name__ == "__main__":
    head = create_list()

    current = head

    while current:
        print(current.data)
        current = current.next