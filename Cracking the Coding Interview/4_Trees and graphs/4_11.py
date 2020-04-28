# Random Node: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete,
# has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen.
# Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.

# Comment: it's also possible with random.choice(seq)– returns pseudo-random element from non-empty sequences

from random import randint

class Node():
    def __init__(self, node):
        self.val = node
        self.left = None
        self.right = None


class binSTree():
    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root == None:
            self.root = Node(node)
        else:
            self._insert(node, self.root)

    def _insert(self, node, root):
        if node < root.val:
            if root.left != None:
                self._insert(node, root.left)
            else:
                root.left = Node(node)
        else:
            if root.right != None:
                self._insert(node, root.right)
            else:
                root.right = Node(node)

    def find(self, node):
        while self.root:
            if node == self.root.val:
                return self.root.val
            elif node < self.root.val:
                if self.root.left:
                    self.root = self.root.left
                else:
                    return False
            elif node > self.root.val:
                if self.root.right:
                    self.root = self.root.right
                else:
                    return False

    #def delete(self, node):
    #    if not self.find(node):
    #        return False
    #   node_to_delete = self.find(node)

    def inOrderTraverse(self, root):
        if root is None:
            return []
        return self.inOrderTraverse(root.left) + [root.val] + self.inOrderTraverse(root.right)


    def getRandomNode(self):
        arr = self.inOrderTraverse(self.root)
        print(arr)

        ran = randint(0, len(arr))
        return arr[ran]


if __name__ == "__main__":
    tree1 = binSTree()
    list1 = [3, 4, 0, 8, 2]
    for node in list1:
        tree1.insert(node)

    print(tree1.getRandomNode())
