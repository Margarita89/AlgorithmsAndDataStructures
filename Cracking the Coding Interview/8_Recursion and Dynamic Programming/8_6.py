# Towers of Hanoi: In the classic problem of the Towers of Hanoi,
# you have 3 towers and N disks of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom
# (i.e., each disk sits on top of an even larger one). You have the following constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks.


def towersOfHanoi(stack1, stack2, stack3, n):
    print('0 : ', stack1, stack2, stack3, n)
    if n == 2:
        # transfer 1-2 from stack1 to stack3
        stack2.append(stack1.pop())
        stack3.append(stack1.pop())
        stack3.append(stack2.pop())
        return stack1, stack2, stack3
    if n == 1:
        stack3.append(stack1.pop())
        return stack1, stack2, stack3
    if n == 0:
        raise Exception("Empty tower 1")
    # move (n-1) element to stack3
    stack1, stack2, stack3 = towersOfHanoi(stack1, stack3, stack2, n-1)
    print('1 : ', stack1, stack2, stack3, n)
    # move last element to stack2
    stack2.append(stack1.pop())
    print('2 : ', stack1, stack2, stack3, n)
    # move all n-1 elements to stack2 which contains last element + change towers
    stack2, stack1, stack3 = towersOfHanoi(stack3, stack1, stack2, n-1)
    print('3 : ', stack1, stack2, stack3, n)

    return stack1, stack2, stack3


if __name__ == "__main__":
    n = 4
    list = [i for i in range(n)]
    stack1 = []
    stack2 = []
    stack3 = []
    for i in range(n-1,-1,-1):
        stack1.append(list[i])
    print(stack1, stack2, stack3)

    print(towersOfHanoi(stack1, stack2, stack3, n))


