# Permutations without Dups: Write a method to compute all permutations of a string of unique characters.


def get_Permutations(prefix, remain, ans):
    if len(remain) == 0:
        ans.append(prefix)
        return ans
    for i in range(len(remain)):
        ans = get_Permutations(prefix + remain[i], remain[:i] + remain[i+1:], ans)
    return ans


def Permutations(s):
    ans = []
    get_Permutations('', s, ans)
    return ans


if __name__ == "__main__":
    s = 'abcd'
    print("Permutations of", s, 'are', ', '.join(Permutations(s)))
