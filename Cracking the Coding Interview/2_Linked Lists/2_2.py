# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

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


# return elements from k to last
def ReturnKthtoLast(linkedList, k):
    counter = 1
    cur = linkedList.head

    while cur is not None:
        if counter == k:
            return cur
        else:
            counter += 1
            cur = cur.next
    if counter < k:
        print("Number of elements in the list is less than k")
        return


if __name__ == "__main__":
    list1 = [1, 2, 5, 1, 3, 5, 4]
    list2 = ['a', 'b', 'c', 'd', 'c', 'e', 'f', 'b']
    list3 = ['vivek', 'sid', 'vignesh', 'nik', 'smriti', 'vivek', 'prateek', 'nik']
    k = 4

    #create list
    l = LinkedList(list1)
    l.printList()
    cur = ReturnKthtoLast(l, k)
    print(cur.val)

    l = LinkedList(list2)
    l.printList()
    cur = ReturnKthtoLast(l, k)
    print(cur.val)

    l = LinkedList(list3)
    l.printList()
    cur = ReturnKthtoLast(l, k)
    print(cur.val)
