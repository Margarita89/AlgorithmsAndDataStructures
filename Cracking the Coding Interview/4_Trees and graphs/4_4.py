# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

# A binary tree Node
class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Find height of the binary tree
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


# Check if binary tree is balanced (max difference is 1)
def checkBalanced(root):

    if root is None:
        return 0, True

    height_left, isBalanced_left = checkBalanced(root.left)
    height_right, isBalanced_right = checkBalanced(root.right)

    if not isBalanced_left or not isBalanced_right or abs(height_left - height_right) > 1:
        return 0, False

    # return height of the root
    return max(height_right, height_left) + 1, True


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)


    diff, isBalanced = checkBalanced(root)
    print(isBalanced)

    root.left.left.right = Node(7)
    root.left.left.right.left = Node(8)

    diff, isBalanced = checkBalanced(root)
    print(isBalanced)


