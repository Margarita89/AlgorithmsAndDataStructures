# Intersection: Given two (singly) linked lists, determine if the two lists intersect.
# Return the intersecting node. Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference)
# as the jth node of the second linked list, then they are intersecting.

# Comment: loops l1 and l2, pointers are divided properly and then run until end of the shortest

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


# check for intersection
def Intersection(l1, l2):
    cur1 = l1.head
    cur2 = l2.head

    len1 = 0
    len2 = 0
    # find both linked lists lengths
    while cur1:
        len1 += 1
        cur1 = cur1.next
    while cur2:
        len2 += 1
        cur2 = cur2.next
    # return pointers to the beginning
    cur1 = l1.head
    cur2 = l2.head
    # move pointer so the end length is the same for both lists
    if len1 > len2:
        for i in range(len1 - len2):
            cur1 = cur1.next
    elif len2 > len1:
        for i in range(len2 - len1):
            cur2 = cur2.next
    # find beginning of intersection
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    if cur1 is None:
        return False
    return True


if __name__ == '__main__':
    list1 = [1, 2, 2, 1, 3]
    list2 = [9, 3, 5, 1, 3, 5, 4]
    list3 = [8, 7]

    l1 = LinkedList(list1)
    l2 = LinkedList(list1)
    l3 = LinkedList(list3)

    cur1 = l1.head
    while cur1.next:
        cur1 = cur1.next
    cur1.next = l2.head

    cur3 = l3.head
    while cur3.next:
        cur3 = cur3.next
    cur3.next = l2.head

    l1.printList()
    l3.printList()
    key = Intersection(l1, l3)
    print(key)

