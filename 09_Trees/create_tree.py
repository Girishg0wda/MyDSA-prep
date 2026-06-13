class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    root = TreeNode(10)

    root.left = TreeNode(5)
    root.right = TreeNode(15)

    return root


if __name__ == "__main__":
    root = create_tree()

    print(root.data)
    print(root.left.data)
    print(root.right.data)