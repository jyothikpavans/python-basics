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


def matrix_multiplication(m1: list, m2: list):
    if r1 != c2:
        print("Invalid input.")
    else:
        multiply_matrix = []
        for i in range(r1):
            x = []
            for j in range(c2):
                x.append(0)
            multiply_matrix.append(x)
        print(multiply_matrix)
        for i in range(r1):
            for j in range(c2):
                sum_elements = 0
                for k in range(c1):
                    sum_elements = sum_elements + (matrix_one[i][k] * matrix_two[k][j])
                multiply_matrix[i][j] = sum_elements
    print(multiply_matrix)
    return multiply_matrix


r1 = int(input("Please Enter number of rows: "))
c1 = int(input("Please Enter number of columns: "))

matrix_one = matrix_input(r1, c1)
# print_matrix(matrix_one)

r2 = int(input("Please Enter number of rows: "))
c2 = int(input("Please Enter number of columns: "))

matrix_two = matrix_input(r2, c2)
# print_matrix(matrix_two)
print_matrix(matrix_multiplication(matrix_one, matrix_two))
