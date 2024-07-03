n = int(input("Please Enter a natural number: "))

for row in range(1, n + 1):
    for column in range(1, row + 1):
        if row < 3 or row == n:
            print("*", end='')
        else:
            if column == 1 or column == row:
                print("*", end='')
            else:
                print(" ", end='')
    print()


