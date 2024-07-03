n = int(input("Please Enter a natural number: "))

for row in range(n, 0, -1):
    first_number_in_row = 1
    for column in range(1, n + 1):
        if column == row or column > row:
            print(first_number_in_row, end='')
            first_number_in_row += 1
        else:
            print(" ", end='')
    print()

