# Palindrome: Implement a function to check if a linked list is a palindrome.
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

    def add(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node

    def printList(self):
            node = self.head
            while node is not None:
                print(node.val, end=' ')
                node = node.next
            print()

# checks if a list is a palindrome
def Palindrome(linkedList):
    # mid will be the middle

    l = LinkedList([])
    mid = linkedList.head
    fast = linkedList.head

    # find middle
    while fast.next is not None:
        mid = mid.next
        fast = fast.next.next

    # insert second half of the list in a new list from head
    while mid is not None:
        l.add(mid.val)
        mid = mid.next

    cur = l.head
    cur2 = linkedList.head
    # compare two lists
    while cur is not None:
        if cur.val != cur2.val:
            return False
        cur = cur.next
        cur2 = cur2.next

    return True


if __name__ == '__main__':

    list1 = [1, 2, 5, 1, 3, 5, 4]
    list2 = [1, 2, 3, 2, 1]
    list3 = ['vivek', 'sid', 'vignesh', 'nik', 'smriti', 'vivek', 'prateek', 'nik']

    l = LinkedList(list1)
    l.printList()
    print(Palindrome(l))

    l = LinkedList(list2)
    l.printList()
    print(Palindrome(l))
