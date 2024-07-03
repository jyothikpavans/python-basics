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


def add_matrices(m1: list, m2: list):
    # initialise sum Matrix
    sum_matrix = []
    if r1 != r2 or c1 != c2:
        print(" You cannot add 2 matrices which have different rows or columns. ")
    else:
        for rows in range(0, r1):
            row = []
            for columns in range(0, c2):
                row.append(m1[rows][columns] + m2[rows][columns])
            sum_matrix.append(row)
    return sum_matrix


r1 = int(input("Please Enter number of rows: "))
c1 = int(input("Please Enter number of columns: "))

matrix_one = matrix_input(r1, c1)
# print_matrix(matrix_one)

r2 = int(input("Please Enter number of rows: "))
c2 = int(input("Please Enter number of columns: "))

matrix_two = matrix_input(r2, c2)
# print_matrix(matrix_two)

sum_matrix = add_matrices(matrix_one, matrix_two)
if len(sum_matrix)>0:
    print_matrix(sum_matrix)

