# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?


# in place rotation by 90 degrees right
def rotateMatrix(m):
    R = len(m) - 1
    C = len(m[0]) - 1

    for i in range(round(R/2)+1):
        for j in range(round(C/2)):
            m[i][j], m[j][C-i], m[C-i][R-j], m[R-j][i] = m[R-j][i], m[i][j], m[j][C-i], m[C-i][R-j]
    return m


if __name__ == "__main__":

    # matrix input from user

    #R = int(input("Enter the number of rows:"))
    #C = int(input("Enter the number of columns:"))
    R = 5
    C = 5

    # Initialize matrix
    matrix = []
    #print("Enter the entries rowwise:")

    # For user input
    for i in range(R):          # A for loop for row entries
        a = []
        for j in range(C):      # A for loop for column entries
             #a.append(int(input()))
            a.append(i * R + j)
        matrix.append(a)

    if R == 1 and C == 1:
        print(matrix)
    else:
        print(rotateMatrix(matrix))
