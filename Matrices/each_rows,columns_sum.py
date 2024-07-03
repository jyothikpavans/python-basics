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


def print_sum_each_row_each_column(matrix: list):
    r = len(matrix)
    c = len(matrix[0])
    print("Row Sums ",end='')
    for row in range(0, r):
        sum_each_row = 0
        for column in range(0, c):
            sum_each_row += matrix[row][column]
        print(sum_each_row, end=' ')
    print()
    print("Column Sums ",end='')
    for column in range(0, c):
        sum_each_column = 0
        for row in range(0, r):
            sum_each_column += matrix[row][column]
        print(sum_each_column, end=' ')


r = int(input("Please Enter no. of rows: "))
c = int(input("Please Enter no. of columns: "))
print_sum_each_row_each_column(matrix_input(r, c))
