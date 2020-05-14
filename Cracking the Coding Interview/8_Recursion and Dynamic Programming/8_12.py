# Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board so that none of them
# share the same row, column, or diagonal.
# In this case, "diagonal" means all diagonals, not just the two that bisect the board.

import copy

# checks if existing points intersect with (r,c) on diagonal or on row
def check_diag_column(r, c, column):
    for i in range(r):
        # check if existing points intersect with (r,c) on row
        if c == column[i]:
            return False
        # check if existing points intersect with (r,c) on diagonal or
        if abs(r - i) == abs(c - column[i]):
            return False
    return True


def eight_queens(n, r, column, results):
    if r == 8:
        results.append(copy.copy(column))
    else:
        for j in range(n):
            if check_diag_column(r, j, column):
                column[r] = j
                eight_queens(n, r + 1, column, results)


def queens(n):
    results = []
    for i in range(n):
        # insert queen into column[row_num] = col_num
        column = [-1] * n
        column[0] = i
        eight_queens(n, 1, column, results)
    return results


if __name__ == "__main__":
    n = 8
    results = queens(n)
    print('All ways of arranging eight queens:', results)
    print('Number of ways:', len(results))
