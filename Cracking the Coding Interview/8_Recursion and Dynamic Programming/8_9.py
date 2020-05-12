# Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parentheses.

# EXAMPLE
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()


def get_parens(n):
    all_parens = set()
    # base case
    if n == 1:
        all_parens.add('()')
        return all_parens
    # general case
    prev_parens = get_parens(n-1)
    for prev in prev_parens:
        for i in range(len(prev)):
            all_parens.add(prev[:i] + '()' + prev[i:])
    return all_parens


if __name__ == "__main__":
    n = 3
    print(list(get_parens(n)))
