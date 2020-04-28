# Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of Tl.

class Node():
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None


def findSubtree(root):
    if root is None:
        return [None]
    return [root.val] + findSubtree(root.left) + findSubtree(root.right)


def CheckSubTree(t1, t2):
    subtree1 = findSubtree(t1)
    subtree2 = findSubtree(t2)

    if subtree1 == subtree2:
        return True

    print(subtree1)
    print(subtree2)

    for i in range(len(subtree1) - len(subtree2) + 1):
        if subtree1[i:i+len(subtree2)] == subtree2:
            return True
    return False


if __name__ == "__main__":

    root = Node(4)
    root.left = Node(1)
    root.right = Node(5)
    root.left.left = Node(0)
    root.left.right = Node(2)
    root.right.right = Node(6)

    root2 = Node(1)
    root2.left = Node(0)
    root2.right = Node(2)

    print(CheckSubTree(root, root2))
