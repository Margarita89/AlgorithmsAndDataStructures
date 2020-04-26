# Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.
class Stack():

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def top(self):
        return self.stack[-1]


def SortStack(stack):
    # create an empty additional temporal stack
    temp_stack = Stack()

    while not stack.isEmpty():
        x = stack.pop()

        # while temporary stack is not empty and the last is less than x
        while not temp_stack.isEmpty() and temp_stack.top() < x:

            # return all items back to stack
            stack.push(temp_stack.pop())

        # now it's time to push x
        temp_stack.push(x)

    return temp_stack


if __name__ == "__main__":

    # create sorted_stack
    stack = Stack()

    stack.push(4)
    stack.push(105)
    stack.push(23)
    stack.push(8)
    stack.push(87)
    stack.push(52)

    stack2 = SortStack(stack)

    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())


