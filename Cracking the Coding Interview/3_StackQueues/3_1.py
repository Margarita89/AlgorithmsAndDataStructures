# Three in One: Describe how you could use a single array to implement three stacks
class threeStacks():

    def __init__(self, n):
        # size of the array
        self.n = n

        # array of size n to allocate 3 stacks
        self.array = [0] * self.n

        # array of top indexes for 3 stacks, initialized with '-1'
        self.top = [-1] * 3

        # array to store indexes for the next item in the stack, last index points nowhere
        self.next = [i+1 for i in range(self.n)]
        self.next[self.n-1] = -1

        # stack to point to next free index in the array, initially it's 0 (first index)
        self.free = 0

    # Return true if and only if the stack is empty
    def isEmpty(self, k_stack):
        return self.top[k_stack] == -1

    # Return true if array is full (free is -1 which means no free spaces)
    def isFull(self):
        return self.free == -1

    # Add an item to the top of the stack (k_stack)
    def push(self, k_stack, item):
        # check if there is free place:
        if self.isFull():
            print('Array is full')
            return ()

        # get free index
        index = self.free

        # update free
        self.free = self.next[index]

        # insert into array by index
        self.array[index] = item

        # update next such it points to top (which is now it's next item), might be -1 if it's first item of stack
        self.next[index] = self.top[k_stack]

        # update last index of k_stack in top
        self.top[k_stack] = index

    # Remove the top item from the stack
    def pop(self, k_stack):
        # check if stack is empty
        if self.isEmpty(k_stack):
            print('The stack is Empty')
            return

        # get the top index
        top_index = self.top[k_stack]

        # update top with the index from next (as required by pop() method)
        self.top[k_stack] = self.next[top_index]

        # update next - now it points again to the next free space
        self.next[top_index] = self.free

        # update free by returning top_index as a free space
        self.free = top_index

        # return the item by top_index
        return self.array[top_index]

    # Return the top of the stack
    def peek(self, k_stack):
        # check if stack is empty
        if self.isEmpty(k_stack):
            print('The stack is Empty')
            return

        # get the top index
        top_index = self.top[k_stack]

        # return the item by top_index
        return self.array[top_index]

    # print stack
    def printStack(self, k_stack):
        # check if stack is empty
        if self.isEmpty(k_stack):
            print('The stack is Empty')
            return

        while not isEmpty(k_stack):
            item = self.pop(k_stack)
            print(item, end=', ')

    # another option
    def printStack2(self, k_stack):
        top_ind = self.top[k_stack]
        while top_ind != -1:
            item = self.array[top_ind]
            print(item, end=', ')
            top_ind = self.next[top_ind]
        print()

if __name__ == "__main__":

    # Create threeStacks with array n=10
    stacks = threeStacks(10)

    # Push items to stack number 2.
    stacks.push(2, 12)
    stacks.push(2, 13)
    stacks.push(2, 6)
    stacks.push(2, 7)
    stacks.printStack2(2)

    # Push items to stack number 1.
    stacks.push(1, 36)
    stacks.push(1, 4)
    stacks.printStack2(1)

    # Push items to stack number 0.
    stacks.push(0, 2)
    stacks.push(0, 89)
    stacks.printStack2(0)

    # Pop from stacks
    stacks.pop(2)
    stacks.pop(2)
    stacks.printStack2(2)

    stacks.pop(1)
    stacks.printStack2(1)

    stacks.pop(0)
    stacks.printStack2(0)

    # Push items to stack 0
    stacks.push(0, 25)
    stacks.push(0, 198)

    stacks.printStack2(0)
