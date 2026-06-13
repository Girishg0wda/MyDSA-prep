from create_tree import create_tree

root = create_tree()


def inorder(node):
    if not node:
        return

    inorder(node.left)

    print(node.data)

    inorder(node.right)


inorder(root)