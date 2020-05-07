# The Egg Drop Problem: There is a building of 100 floors. If an egg drops from the Nth floor or above, it will break.
# If it's dropped from any floor below, it will not break.
# You're given two eggs. Find N, while minimizing the number of drops for the worst case.

# Minimum number of trials for the worst case
def eggDrop(eggs, steps):
    # base cases
    if steps == 1 or steps == 0:
        return steps
    if eggs == 1:
        return steps

    min_drops = float('inf')

    # either broken (then explore x-1 steps) or not broken (explore the rest of steps: steps - x)
    for x in range(1, steps+1):
        drops = max(eggDrop(eggs - 1, x - 1), eggDrop(eggs, steps - x))
        min_drops = min(drops, min_drops)

    return min_drops + 1    # add the previous step


if __name__ == "__main__":

    eggs = 2
    stairs = 20
    print("Minimum number of trials in worst case with",
           eggs, "eggs and", stairs, "floors is", eggDrop(eggs, stairs))
