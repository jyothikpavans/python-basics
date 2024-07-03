n = int(input("Please Enter a natural number: "))

number = n
previous_column = 1
next_column = 2 * n

for row in range(1, n + 1):
    for column in range(1,  2 * n):
        if column in range(previous_column, next_column):
            print("*", end='')
        else:
            print(" ", end='')
    previous_column += 1
    next_column -= 1
    print()

number = n
previous_column = n - 1
next_column = n + 2

for row in range(1, n):
    for column in range(1, 2 * n):
        if column in range(previous_column, next_column):
            print("*", end='')
        else:
            print(" ", end='')
    previous_column -= 1
    next_column += 1
    print()



