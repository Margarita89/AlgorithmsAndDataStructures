#  Stack Min: How would you design a stack which,
#  in addition to push and pop, has a function min which returns the minimum element?
#  Push, pop and min should all operate in 0(1) time.

# Comment: better solution (with less space) supports only new_min. If the added item > cur_min, add NOthing to stack_of_min
# when .pop(), pop from stack_of_min ONLY of the item is equal to the top item in stack_of_min
# Attention: if there are several cur_min items - add and remove them every time

class stackMin():

    def __init__(self):
        # initialize empty stack
        self.stack = []
        self.stack_of_min = []
        self.cur_min = float('inf')

    def push(self, x):
        self.stack.append(x)
        if x < self.cur_min:
            self.stack_of_min.append(x)
            self.cur_min = x
            print('x : ', x)
        else:
            self.stack_of_min.append(self.cur_min)
            print('cur_min :', self.cur_min)

    def pop(self):
        x = self.stack[-1]
        del self.stack[-1]
        del self.stack_of_min[-1]
        return x

    def get_min(self):
        return self.stack_of_min[-1]


if __name__ == "__main__":

    stack_new = stackMin()

    # Push items to stack
    stack_new.push(12)
    stack_new.push(13)
    print(stack_new.get_min())
    stack_new.push(6)
    stack_new.push(7)
    print(stack_new.get_min())

    #print(stack)

    # Pop items from stack
    stack_new.pop()
    print(stack_new.get_min())
    #print(stack)
#    print(stack_of_min)
    stack_new.pop()
    print(stack_new.get_min())
    #print(stack)

    stack_new.pop()
    print(stack_new.get_min())

