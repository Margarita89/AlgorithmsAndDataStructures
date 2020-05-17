# Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending order,
# write a method to find an element.


def sorted_matrix_search(matrix, N, M, elem):
    i, j = 0, N - 1
    while i < M and j >= 0:
        if matrix[i][j] == elem:
            return i, j
        # eliminate i-th row from search
        if matrix[i][j] < elem:
            i += 1
        # eliminate last column from search
        else:
            j -= 1
    return -1, -1


if __name__ == "__main__":
    N = 3
    M = 4
    matrix = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            matrix[i][j] = i + j * M
    print('Sorted Matrix :', matrix)
    elem = 9

    row, column = sorted_matrix_search(matrix, N, M, elem)
    if row == -1:
        print('Element was not found')
    else:
        print('Indexes of element', elem,'are:', row, column)
