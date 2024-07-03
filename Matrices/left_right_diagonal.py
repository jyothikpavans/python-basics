def matrix_input(r: int, c: int):
    # initialise Matrix
    matrix = []
    print("Enter the entries row wise: ")

    # For user input
    for i in range(r):  # a loop for row entries.
        a = []
        for j in range(c):  # a loop for column entries.
            a.append(int(input()))
        matrix.append(a)
    return matrix


def print_left_diagonal_matrix(matrix: list):
    print("Left Diagonal Elements ", end='')
    r = len(matrix)
    c = len(matrix[0])
    for row in range(0, r):
        for column in range(0, c):
            if row == column:
                print(matrix[row][column], end=' ')
    print()


def print_right_diagonal_matrix(matrix: list):
    print("Right Diagonal Elements ", end='')
    r = len(matrix)
    c = len(matrix[0])
    size_matrix = r * c
    for row in range(0, r):
        for column in range(0, c):
            if row + column == r - 1:
                print(matrix[row][column], end=' ')


r = int(input("Please Enter no. of rows: "))
c = int(input("Please Enter no. of columns: "))
if r == c:
    input_matrix = matrix_input(r, c)
    print_left_diagonal_matrix(input_matrix)
    print_right_diagonal_matrix(input_matrix)
else:
    print("Rows and columns should be equal")
