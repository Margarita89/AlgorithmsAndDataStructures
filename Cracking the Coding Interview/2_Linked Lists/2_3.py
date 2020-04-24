# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.

# Node class
class Node():

    # Constructor to initialize the node object
    def __init__(self, x):
        self.val = x
        self.next = None

# LinkedList class
class LinkedList():
    """Create singly linked list by passing the list to the constructor"""
    def __init__(self, linkedList):
        self.head = None
        self.insert(linkedList)

    def insert(self, linkedList):
        # reverse as inserting from head (from left)
        for x in reversed(linkedList):
            node = Node(x)
            node.next = self.head
            self.head = node

    def printList(self):
            node = self.head
            while node is not None:
                print(node.val, end=' ')
                node = node.next
            print()

# deletes node by it's key
def deleteMiddleNode(key):
    # check if it's last node
    if key.next is None:
        return
    # temp is the next elem in the list
    temp = key.next
    # copy val from temp to key
    key.val = temp.val
    # key pointer to the next after temp, skip temp
    key.next = temp.next


if __name__ == '__main__':

    list1 = [1, 2, 5, 1, 3, 5, 4]
    list2 = ['a', 'b', 'c', 'd', 'c', 'e', 'f', 'b']
    list3 = ['vivek', 'sid', 'vignesh', 'nik', 'smriti', 'vivek', 'prateek', 'nik']

    l = LinkedList(list1)
    l.printList()
    cur = l.head
    key = cur.next.next.next
    print(key)
    deleteMiddleNode(key)
    l.printList()


