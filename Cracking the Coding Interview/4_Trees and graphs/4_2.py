# Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height.

class Node():
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


def MinimalTree(array, start, end):
    if start > end:
        return
    mid = (end + start) // 2
    root = Node(array[mid])
    print(root.node)
    root.left = MinimalTree(array, start, mid - 1)
    root.right = MinimalTree(array, mid + 1, end)
    return root


if __name__ == "__main__":
    test_sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    MinimalTree(test_sorted_array, 0, len(test_sorted_array) - 1)
