# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop() should return the same values as it would if there were just a single stack).

# Comment: is it worth removing stack from stacks when the item is popped?

# Comment: try to implement shift in recursion

class setOfStacks():

    def __init__(self, threshould):
        # lists of lists for stacks
        self.stacks = [[]]
        self.threshold = threshould
        # initialize a counter of stacks
        self.stack_counter = 0

    # check if the current stack is full
    def isFull(self, k_stack):
        return len(self.stacks[k_stack]) == self.threshold

     # check if the current stack is empty
    def isEmpty(self, k_stack):
        return len(self.stacks[k_stack]) == 0

    # push into available stack
    def push(self, x):
        # check if the previous stack if Full
        if self.isFull(self.stack_counter):
            # add new stack empty stack
            self.stacks.append([])
            # increase stack_counter for the new stack
            self.stack_counter += 1
            # append new item to the new stack
            self.stacks[self.stack_counter].append(x)

        else:
            self.stacks[self.stack_counter].append(x)


    def pop(self):
        # check if current stack is already empty
        if self.isEmpty(self.stack_counter):
            self.stack_counter -= 1
        if self.stack_counter >= 0:
            return self.stacks[self.stack_counter].pop()
        else:
            print('There are no Plates left')
            return


    def popAt(self, k_stack):
        # if it's the last stack - then usual pop method
        if k_stack == self.stack_counter:
            return self.stacks.pop()
        else:
            print('k_stack : ', k_stack)
            x = self.stacks[k_stack].pop()
            self.shift_stacks(k_stack)
            return x

    # shift stacks by 1 item after popAt starting from k_stack
    def shift_stacks(self, k_stack):
        temp = []
        # starting from k_stack+1
        i = k_stack + 1

        while i <= self.stack_counter and not self.isEmpty(self.stack_counter):
            while not self.isEmpty(i):
                x = self.stacks[i].pop()
                temp.append(x)
            # append to previous stack
            y = temp.pop()
            self.stacks[i-1].append(y)
            while temp:
                x = temp.pop()
                self.stacks[i].append(x)
            i += 1

        # check if after rolling the last stack became empty
        if self.isEmpty(self.stack_counter):
            self.stack_counter -= 1


if __name__ == "__main__":
    # create stacks and appoint threshold = 4
    stacks = setOfStacks(3)

    # push items to stacks
    stacks.push(4)
    stacks.push(5)
    stacks.push(3)
    stacks.push(42)
    stacks.push(51)

    stacks.push(29)
    stacks.push(81)

    print(stacks.pop())
    print(stacks.pop())
#    print(len(stacks))

    print(stacks.popAt(0))
 #   print(len(stacks))
    print(stacks.pop())

    print(stacks.popAt(0))

    stacks.push(1029)
    stacks.push(8100)
    stacks.push(7)
    stacks.push(27)
    stacks.push(47)

    print(stacks.popAt(1))
