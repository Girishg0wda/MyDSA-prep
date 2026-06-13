from create_tree import create_tree

root = create_tree()


def postorder(node):
    if not node:
        return

    postorder(node.left)
    postorder(node.right)

    print(node.data)


postorder(root)