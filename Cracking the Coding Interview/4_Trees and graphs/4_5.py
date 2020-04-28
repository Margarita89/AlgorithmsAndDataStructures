# Validate BST: Implement a function to check if a binary tree is a binary search tree.

# Recursive solution // it's also possible to use simple inOrder

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Compare root.val to min_tree and max_tree
def ValidateBST_recursive(root, min_tree, max_tree):
    if root is None:
        return True

    # check if root.val doesn't belong to interval (min_tree, max_tree]
    if (root.val < min_tree) or (root.val > max_tree):
        return False

    # return check for root.left and root.right
    return ValidateBST_recursive(root.left, min_tree, root.val-1) and ValidateBST_recursive(root.right, root.val+1, max_tree)


def CheckBST(root):
    min_tree = -float('inf')
    max_tree = float('inf')
    return ValidateBST_recursive(root, min_tree, max_tree)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)
    print(CheckBST(root))

    root.left.left.right = Node(17)
    root.left.left.right.left = Node(8)
    print(CheckBST(root))

