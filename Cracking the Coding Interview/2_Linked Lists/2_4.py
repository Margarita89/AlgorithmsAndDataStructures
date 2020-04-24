# Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than or equal to x.
# If x is contained within the list, the values of x only need to be after the elements less than x (see below).
# The partition element x can appear anywhere in the "right partition";
# it does not need to appear between the left and right partitions.

# The idea1 : put all smaller elements to the head
# The idea2: create 2 separate lists: less and larger than x and then combine them

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

    def printList(self):
        node = self.head
        while node is not None:
            print(node.val, end=' ')
            node = node.next
        print()


def Partition(linkedList, part_x):

    runner = linkedList.head.next
    prev = linkedList.head

    all_small = prev.val < part_x

    while runner is not None:
        # move smaller element to head
        if runner.val < part_x and not all_small:
            prev.next = prev.next.next
            runner.next = linkedList.head
            linkedList.head = runner
            # update runner
            runner = prev.next

        else:
            all_small = False
            # move runner and prev forward
            runner = runner.next
            prev = prev.next

    linkedList.printList()

def Partition2(linkedList, part_x):
    # create before and after lists with dummy nodes
    runner = linkedList.head
    l_smaller = Node(0)
    cur_smaller = l_smaller
    l_larger = Node(0)
    cur_larger = l_larger

    # fill in before and after lists
    while runner:
        if runner.val < part_x:
            cur_smaller.next = runner
            cur_smaller = cur_smaller.next
        else:
            cur_larger.next = runner
            cur_larger = cur_larger.next
        runner = runner.next

    cur_larger.next = None
    cur_smaller.next = l_larger.next

    return l_smaller.next


if __name__ == '__main__':

    list1 = [1, 2, 5, 1, 3, 5, 4]
    part_x1 = 5
    list2 = ['a', 'b', 'c', 'd', 'c', 'e', 'f', 'b']
    part_x2 = 'd'
    #list3 = ['vivek', 'sid', 'vignesh', 'nik', 'smriti', 'vivek', 'prateek', 'nik']
    examples = [(list1, part_x1), (list2, part_x2)]

    for lists, parts in examples:
        l = LinkedList(lists)
        l.printList()
        cur = Partition2(l, parts)
        #l.printList()
        while cur is not None:
            print(cur.val, end =' ')
            cur = cur.next
        print()
