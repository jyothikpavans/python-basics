n = int(input("Please Enter a natural number: "))
for row in range(n, 0, -1):
    for column in range(1, n + 1):
        if column == row or column > row:
            print("*", end='')
        else:
            print(" ", end='')
    print()

first_column = 1
for row in range(1, n):
    for column in range(1, n + 1):
        if column <= first_column:
            print(" ", end='')
        else:
            print("*", end='')
    first_column += 1
    print()


