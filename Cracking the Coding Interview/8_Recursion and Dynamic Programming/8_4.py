# Power Set: Write a method to return all subsets of a set

# Idea: generating all binary numbers from 0 to 2 ** n - 1
# corresponding to include (=1)/ not include (=0)

def get_subset(set_for_power, x):
    subset = []
    index = 0
    while x:
        if x & 1 == 1:
            subset.append(set_for_power[index])
        x = x >> 1
        index += 1
    return subset


def power_set(set_for_power):
    allsubsets = []
    max_len = 2 ** len(set_for_power)
    for i in range(max_len):
        subset = get_subset(set_for_power, i)
        allsubsets.append(subset)
    return allsubsets


if __name__ == "__main__":
    set_for_power = [1, 2, 3, 5]
    print(power_set(set_for_power))
