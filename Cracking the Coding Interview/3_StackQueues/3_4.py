# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
class queueViaStacks():

    def __init__(self):
        self.stack_left = []
        self.stack_right = []

    # Add an item to the end of the list
    def add(self, x):
        if self.isEmpty(1):
            self.stack_left.append(x)
        else:
            while not self.isEmpty(1):
                y = self.stack_left.pop()
                self.stack_right.append(y)
            self.stack_right.append(x)
            while not self.isEmpty(2):
                z = self.stack_right.pop()
                self.stack_left.append(z)

    # Remove the first item in the list
    def remove(self):
        if self.isEmpty(1):
            print('Queue is empty')
            return
        return self.stack_left.pop()

    # Return the top of the queue
    def peek(self):
        while not self.isEmpty(1):
            x = self.stack_left.pop()
            self.stack_right.append(x)
        peek_item = self.stack_right.pop()
        self.stack_right.append(peek_item)

        while not self.isEmpty(2):
            y = self.stack_right.pop()
            self.stack_left.append(y)
        return peek_item

    # Return true if and only if the queue is empty
    def isEmpty(self, stack_num):
        if stack_num == 1:
            x = len(self.stack_left)
        else:
            x = len(self.stack_right)
        if x == 0:
            return True
        else:
            return False


if __name__ == "__main__":

    queue = queueViaStacks()

    # Add items to queue
    queue.add(12)
    queue.add(13)
    queue.add(5)

    # Remove items from queue

    print(queue.remove())
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())

    # Add items to queue
    queue.add(12)
    queue.add(13)
    queue.add(5)
    print(queue.remove())

    # Peek
    print(queue.peek())

