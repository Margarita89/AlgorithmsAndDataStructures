# Rank from Stream: Imagine you are reading in a stream of integers.
# Periodically,you wish to be able to look up the rank of a number x
# (the number of values less than or equal to x). Implement the data structures and algorithms to support these operations.
# That is, implement the method track ( int x), which is called when each number is generated,
# and the method getRankOfNumber(int x), which returns the number of values less than or equal tox (not including x itself).


class Node:

    def __init__(self, x):
        self.value = x
        self.left = self.right = None
        self.left_count = 0


# insert x, returns root
def insert(root, x):
    if root is None:
        return Node(x)
    cur = root
    while cur:
        prev = cur
        if cur.value > x:
            cur.left_count += 1
            cur = cur.left
        else:
            cur = cur.right
    if prev.value > x:
        prev.left = Node(x)
    else:
        prev.right = Node(x)
    return root


def in_order(root):
    if root.left is not None:
        in_order(root.left)
    print(root.value, end=' ')
    if root.right is not None:
        in_order(root.right)


def recursive_insert(root, x):
    if root is None:
        return Node(x)
    if root.value > x:
        root.left_count += 1
        root.left = recursive_insert(root.left, x)
    else:
        root.right = recursive_insert(root.right, x)
    return root


# get rank for x in BST
def get_rank(root, x):
    if root.value == x:
        return root.left_count
    if root.value > x:
        if root.left is None:
            return -1
        return get_rank(root.left, x)
    else:
        if root.right is None:
            return 1
        # return all elements on the left + parent (1) + everything from right recursively
        return root.left_count + 1 + get_rank(root.right, x)


def binary_tree_insert(stream):
    root = None
    for x in stream:
        root = recursive_insert(root, x)
    print('In order BST: ', end='')
    in_order(root)
    print()
    return root


if __name__ == "__main__":
    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]

    root = binary_tree_insert(stream)
    num = 1
    print('Rank of Number', num, 'is:', get_rank(root, num))
    num = 5
    print('Rank of Number', num, 'is:', get_rank(root, num))
    num = 13
    print('Rank of Number', num, 'is:', get_rank(root, num))
