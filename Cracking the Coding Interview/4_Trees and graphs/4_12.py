# Paths with Sum: You are given a binary tree in which each node contains an integer value
# (which might be positive or negative).
# Design an algorithm to count the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).

class Node():
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None


def dfs(root, prev_sum, target, cache):
    if not root:
        return 0
    cur_sum = prev_sum + root.val
    count = 0
    if cur_sum - target in cache:
        count += cache[cur_sum - target]
    if cur_sum in cache:
        cache[cur_sum] += 1
    else:
        cache[cur_sum] = 1
    count += dfs(root.left, cur_sum, target, cache)
    count += dfs(root.right, cur_sum, target, cache)
    cache[cur_sum] -= 1     # as this sum is already checked from root
    return count


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(1)
    root.right = Node(5)
    root.left.left = Node(0)
    root.left.right = Node(2)
    root.right.right = Node(-6)

    target = 1
    cache = {}
    print('Number of paths that sum to', target, ':', dfs(root, 0, target, cache))

    root = Node(5)
    root.left = Node(2)
    root.right = Node(1)
    root.left.left = Node(4)
    root.left.right = Node(2)
    root.right.left = Node(3)
    root.right.left.left = Node(1)
    root.right.left.right = Node(5)
    root.right.left.left.left = Node(1)
    root.right.left.left.left.left = Node(4)

    target = 8
    cache = {}
    print('Number of paths that sum to', target, ':', dfs(root, 0, target, cache))


    root = Node(10)
    root.left = Node(5)
    root.right = Node(-3)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.right = Node(11)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right.right = Node(1)

    target = 8
    cache = {}
    print('Number of paths that sum to', target, ':', dfs(root, 0, target, cache))
