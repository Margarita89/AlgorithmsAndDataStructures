# BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

class Node():
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None


def weave(ans, cur, i, j, subtree1, subtree2):
    if cur and len(cur[0]) == len(subtree1) + len(subtree2):
        ans.extend(cur)
        return
    if i < len(subtree1):
        new = [elem + [subtree1[i]] for elem in cur]
        weave(ans, new, i+1, j, subtree1, subtree2)
    if j < len(subtree2):
        new = [elem + [subtree2[j]] for elem in cur]
        weave(ans, new, i, j+1, subtree1, subtree2)


def main_weave(res_s1, res_s2):
    ans = []
    for s1 in res_s1:
        for s2 in res_s2:
            weave(ans, [[]], 0, 0, s1, s2)
    return ans


def recursive(root):
    if not root:
        return [[]]
    res_s1 = recursive(root.left)
    res_s2 = recursive(root.right)
    ans = main_weave(res_s1, res_s2)
    if not ans:
        return [[root.val]]
    return [[root.val] + elem for elem in ans]


if __name__ == "__main__":
    ans = []
    root = Node(4)
    root.left = Node(1)
    root.right = Node(5)
    root.left.left = Node(0)
    root.left.right = Node(2)
    root.right.right = Node(6)

    solution = recursive(root)
    #print(solution)
    for i, item in enumerate(solution):
        print(i, " : ", item)
