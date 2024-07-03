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


def is_matrices_equal(m1: list, m2: list) -> bool:
    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])
    if r1 != r2 or c1 != c2:
        return False

    for rows in range(0, r1):
        for columns in range(0, c1):
            if m1[rows][columns] != m2[rows][columns]:
                return False
    return True


r1 = int(input("Please Enter number of rows: "))
c1 = int(input("Please Enter number of columns: "))

matrix_one = matrix_input(r1, c1)
# print_matrix(matrix_one)

r2 = int(input("Please Enter number of rows: "))
c2 = int(input("Please Enter number of columns: "))

matrix_two = matrix_input(r2, c2)
# print_matrix(matrix_two)

print(is_matrices_equal(matrix_one, matrix_two))
