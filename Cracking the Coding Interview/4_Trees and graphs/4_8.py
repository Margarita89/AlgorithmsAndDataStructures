# First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

class Node():
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None


def firstCommonAncestor(root, node1, node2):
    if root is None:
        return None

    # if at least one of the nodes was found
    if root.val == node1.val or root.val == node2.val:
        return root

    left_anc = firstCommonAncestor(root.left, node1, node2)
    right_anc = firstCommonAncestor(root.right, node1, node2)

    # if both left and right subtrees returned not None means the root is firstCommonAncestor
    if left_anc and right_anc:
        return root

    # else: both nodes are in the left subtree or in the right subtree
    return left_anc if left_anc else right_anc


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)

    node1 = root.left.right
    node2 = root.right.right

    print('firstCommonAncestor of nodes', node1.val, 'and', node2.val, 'is', firstCommonAncestor(root, node1, node2).val)
