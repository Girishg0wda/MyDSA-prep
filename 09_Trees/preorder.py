from create_tree import create_tree

root = create_tree()

def preorder(node):
    if not node:
        return

    print(node.data)

    preorder(node.left)
    preorder(node.right)

preorder(root)