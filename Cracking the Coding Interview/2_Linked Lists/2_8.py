# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
# so as to make a loop in the linked list.


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

# finds if there is a loop
def LoopDetection(l):
    slow = l.head
    fast = l.head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [9, 3, 5, 1, 3, 5, 4]

    l1 = LinkedList(list1)
    # create loop
    loop_start = l1.head.next.next.next
    pointer = l1.head
    while pointer.next is not None:
        pointer = pointer.next
    pointer.next = loop_start
    print(LoopDetection(l1))

