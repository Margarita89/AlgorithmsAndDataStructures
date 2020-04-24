# Remove duplicates from unsorted linked list

# Time complexity O(n), space complexity O(n)

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


# delete repeating nodes using set()
def removeDups(linkedList):

    # create a set to store all values
    list_set = set()

    # initialize cur
    cur = linkedList.head

    list_set.add(cur.val)

    # start with cur.next and run until end
    while cur.next is not None:

        # if not in set - add
        if cur.next.val not in list_set:
            list_set.add(cur.next.val)
            # move cur to next elem
            cur = cur.next

        # if in set - remove from list
        else:
            cur.next = cur.next.next

    linkedList.printList()


if __name__ == "__main__":
    list1 = [1, 2, 5, 1, 3, 5, 4]

    list2 = ['a', 'b', 'c', 'd', 'c', 'e', 'f', 'b']
    list3 = ['vivek', 'sid', 'vignesh', 'nik', 'smriti', 'vivek', 'prateek', 'nik']

    list4 = [1, 1, 1, 1]

    #create list
    l = LinkedList(list1)
    l.printList()
    removeDups(l)

    l = LinkedList(list2)
    l.printList()
    removeDups(l)

    l = LinkedList(list3)
    l.printList()
    removeDups(l)

    l = LinkedList(list4)
    l.printList()
    removeDups(l)
