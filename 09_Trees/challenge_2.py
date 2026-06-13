from create_tree import create_tree

root = create_tree()


def count_nodes(node):
    if not node:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)


print(count_nodes(root))