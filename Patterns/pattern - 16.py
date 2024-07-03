n = int(input("Please Enter a natural number: "))

number = n
previous_column = n
next_column = n

for row in range(1, n + 1):
    for column in range(1, 2 * n):
        if (column == previous_column or column == next_column) or row == n:
            print("*", end='')
        else:
            print(" ", end='')
    previous_column -= 1
    next_column += 1
    print()

