# Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), & (AND), | (OR), and ^ (XOR),
# and a desired boolean result value result, implement a function to count the number of ways of parenthesizing the expression
# such that it evaluates to result.
# The expression should be fully parenthesized (e.g.,(0)^(1)) but not extraneously (e.g.,(((0))^(1))).

# EXAMPLE
# countEval("1^0|0|1", false) -> 2
# countEval("0&0&0&1^1|0", true) -> 10


def countEval(s, res, mem):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return bool(s) == res
    if (res, s) in mem:
        return mem[(res, s)]
    count = 0
    for i in range(1, len(s), 2):
        left = s[:i]
        right = s[i+1:]
        left_True = countEval(left, True, mem)
        left_False = countEval(left, False, mem)
        right_True = countEval(right, True, mem)
        right_False = countEval(right, False, mem)
        total = (left_True + left_False) * (right_True + right_False)
        total_True = 0
        if s[i] == '^':
            total_True = left_True * right_False + left_False * right_True
        elif s[i] == '|':
            total_True = left_True * right_True + left_False * right_True + left_True * right_False
        elif s[i] == '&':
            total_True = left_True * right_True

        if res:
            cur = total_True
        else:
            cur = total - total_True
        count += cur

    mem[(res, s)] = count
    return count


if __name__ == "__main__":
    s = "0&0&0&1^1|0"
    res = True
    mem = {}
    print('Number of ways of parenthesizing the expression', s, 'such that it evaluates to', res, 'is', countEval(s, res, mem))


