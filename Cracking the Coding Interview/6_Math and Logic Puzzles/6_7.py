# The Apocalypse: In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate.
# Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines.
# If all families abide by this policy-that is, they have continue to have children until they have one girl,
# at which point they immediately stop-what will the gender ratio of the new generation be?

import random


def GenderRatio(n_families):
    boys = 0
    girls = 0
    for i in range(n_families):
        girl_in_family = False
        while not girl_in_family:
            child = bool(random.getrandbits(1))
            if child:
                girl_in_family = True
                girls += 1
            else:
                boys += 1
    print("boys : ", boys)
    print("girls : ", girls)
    all_children = boys + girls
    return boys/all_children, girls/all_children


if __name__ == "__main__":
    n_families = 10000
    boys_ratio, girls_ratio = GenderRatio(n_families)
    print("Ratio of girls is : ", girls_ratio)
    print("Ratio of boys is : ", boys_ratio)
