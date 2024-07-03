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


def print_matrix(matrix: list):
    # For printing the Matrix
    r = len(matrix)
    c = len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=' ')
        print()


def transpose_matrix(matrix: list):
    r = len(matrix)
    c = len(matrix[0])
    for rows in range(0, r):
        for columns in range(0, c):
            if rows != columns and rows < columns:
                dummy = matrix[rows][columns]
                matrix[rows][columns] = matrix[columns][rows]
                matrix[columns][rows] = dummy
    return matrix


r = int(input("Please Enter no. of rows: "))
c = int(input("Please Enter no. of columns: "))
print_matrix(transpose_matrix(matrix_input(r, c)))

