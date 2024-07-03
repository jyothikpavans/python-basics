n = int(input("Please Enter a number: "))

for row in range(n, 0, -1):
    for column in range(1, n + 1):
        if row == column or column > row:
            print("*", end='')
        else:
            print(" ", end='')
    print()

