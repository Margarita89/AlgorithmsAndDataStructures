# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zeroMatrix(m):
    # also SET can be used
    dict = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            # add to dict coordinates of zero by row and column separetely
            if m[i][j] == 0:
                # to distinguish between vertical and horizontal
                # if in row - 1
                # if in column - 2
                if i not in dict:
                    dict[i] = 1
                if j not in dict:
                    dict[j] = 2
    for i in range(len(m)):
        for j in range(len(m[0])):
            # all values that intersect with 0 in row or 0 in column become zeros
            # check rows
            if i in dict and dict[i] == 1:
                m[i][j] = 0
            # check columns
            if j in dict and dict[j] == 2:
                m[i][j] = 0
    return m


if __name__ == "__main__":
    # A basic code for matrix input from user

    #R = int(input("Enter the number of rows:"))
    #C = int(input("Enter the number of columns:"))

    R = 5
    C = 5

    # Initialize matrix
    matrix = []
    #print("Enter the entries rowwise:")

    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
             #a.append(int(input()))
            a.append(i * C + j)
        matrix.append(a)

    matrix[0][0] = 1
    matrix[0][2] = 0

    print(matrix)

    if R == 1 and C == 1:
        print(matrix)
    else:
        print(zeroMatrix(matrix))
