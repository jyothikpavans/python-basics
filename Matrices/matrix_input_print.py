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

    # For printing the Matrix
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=' ')
        print()


R = int(input("Please Enter number of rows: "))
C = int(input("Please Enter number of columns: "))
matrix_input(R, C)

