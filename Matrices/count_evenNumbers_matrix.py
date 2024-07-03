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


def print_even_odd_numbers_count_matrix(matrix: list):
    r = len(matrix)
    c = len(matrix[0])
    even_numbers_count = 0
    odd_numbers_count = 0
    for row in range(0, r):
        for column in range(0, c):
            if matrix[row][column] % 2 == 0:
                even_numbers_count += 1
            else:
                odd_numbers_count += 1

    print("No. of Even numbers in the matrix is {0}".format(even_numbers_count))
    print("No. of Odd numbers in the matrix is {0}".format(odd_numbers_count))


r = int(input("Please Enter no. of rows: "))
c = int(input("Please Enter no. of columns: "))
print_even_odd_numbers_count_matrix(matrix_input(r, c))





