# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.


def TripleStep(n):
    if (n == 0) | (n == 1) | (n == 2):
        return n

    a = 1
    b = 1
    c = 2
    for i in range(3, n):
        counter = a + b + c
        a = b
        b = c
        c = counter

    return a + b + c


if __name__ == "__main__":
    # define number of steps
    n = 5
    print(TripleStep(n))
