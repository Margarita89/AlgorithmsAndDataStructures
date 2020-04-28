# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
# You may assume that each node has a link to its parent.

class Node():
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None
        self.parent = None


def SuccessorBST(node):
    if node is None:
        return None

    # if there is a right child - go right and then left until the end
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node.val

    # else: there is no right child - go to parent. If coming from left - it's a successor, if not - continue
    while node.parent:
        if node.parent.left == node:
            return node.parent.val
        node = node.parent

    return None


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.val)
    in_order(root.right)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.left.parent = root
    root.right = Node(7)
    root.right.parent = root
    root.left.left = Node(1)
    root.left.left.parent = root.left
    root.left.right = Node(4)
    root.left.right.parent = root.left
    root.right.left = Node(6)
    root.right.left.parent = root.right
    root.right.right = Node(8)
    root.right.right.parent = root.right

    in_order(root)
    print(f'\n')
    node_pre = root.right.left
    print(SuccessorBST(node_pre))

    root.right.right.right = Node(17)
    root.right.right.right.parent = root.right.right

    node_pre = root.right.right.right
    print(SuccessorBST(node_pre))

    node_pre = root.left.right
    print(SuccessorBST(node_pre))
