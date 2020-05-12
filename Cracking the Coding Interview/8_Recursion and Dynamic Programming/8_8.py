# Permutations with Duplicates: Write a method to compute all permutations of a string whose characters are not necessarily unique.
# The list of permutations should not have duplicates.

from collections import Counter
def get_permutations_dup(hash, prefix, remain, ans):
    if remain == 0:
        ans.append(prefix)
        return ans
    for ch in hash:
        if hash[ch] > 0:
            hash[ch] -= 1
            get_permutations_dup(hash, prefix + ch, remain - 1, ans)
            hash[ch] += 1
    return ans


def permutations(s):
    ans = []
    hash_letters = Counter(s)
    return get_permutations_dup(hash_letters, '', len(s), ans)


if __name__ == "__main__":
    s = 'abca'
    print('Permutations with Duplicates from string =', s, 'are:', permutations(s))
