# Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1 's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.

# Node class
class Node():

    def __init__(self, x):
        self.val = x
        self.next = None


# LinkedList class
class LinkedList():

    def __init__(self, linkedList):
        self.head = None
        self.insert(linkedList)

    def insert(self, linkedList):
        # reverse
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


def sumLists(l1, l2):

    cur1 = l1.head
    cur2 = l2.head

    l = LinkedList([])

    mem_one = 0

    while cur1 is not None or cur2 is not None:
        cur1_val = cur2_val = 0
        if cur1:
            cur1_val = cur1.val
            cur1 = cur1.next
        if cur2:
            cur2_val = cur2.val
            cur2 = cur2.next
        sum = cur1_val + cur2_val + mem_one
        l.add((sum % 10))
        mem_one = sum // 10
    if mem_one == 1:
        l.add(mem_one)

    return l


if __name__ == '__main__':
    list1 = [7, 1, 6]
    list2 = [5, 9, 2]

    l1 = LinkedList(list1)
    l2 = LinkedList(list2)
    l1.printList()
    l2.printList()
    l = sumLists(l1, l2)
    #print(l)
    l.printList()

    list1 = [1, 2, 3, 4]
    list2 = [5, 6, 7]

    len1 = len(list1)
    len2 = len(list2)

    l1 = LinkedList(list1)
    l2 = LinkedList(list2)
    l1.printList()
    l2.printList()
    l = sumLists(l1, l2)
    #print(l)
    l.printList()

