# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

# Idea: recursively go through levels (transfer level_number)

class Binary_Tree():
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


# Node class
class Node():
    def __init__(self, x):
        self.val = x
        self.next = None


# LinkedList class
class LinkedList():
    def __init__(self, x):
        self.head = x
        self.next = None
        #self.insert(x)

    def insert(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node


def listOfDepths(root, lists, level):
    if root is None:
        return
    # check if the level exists in lists, if not create
    if len(lists) == level:
        list = LinkedList(None)
        lists.append(list)
    else:
        list = lists[level]

    list.insert(root.node)

    listOfDepths(root.left, lists, level+1)
    listOfDepths(root.right, lists, level+1)


def MakeLinkedListsOfDepths(root):
    lists = [[]]
    listOfDepths(root, lists, 0)
    return lists


if __name__ == "__main__":
    root = Binary_Tree(5)
    root.left = Binary_Tree(1)
    root.right = Binary_Tree(4)
    root.left.left = Binary_Tree(45)
    root.left.right = Binary_Tree(8)
    root.right.left = Binary_Tree(19)
    root.right.right = Binary_Tree(12)
    root.left.left = Binary_Tree(3)

    print(MakeLinkedListsOfDepths(root))



