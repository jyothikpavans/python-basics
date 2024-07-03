n = int(input("Please Enter a odd natural number: "))

middle_row = (n + 1) / 2
middle_column = (n + 1) / 2

for row in range(1, n + 1):
    for column in range(1, n + 1):
        if row == middle_row:
            print("*", end='')
        else:
            if column == middle_column:
                print("*", end='')
            else:
                print(" ", end='')
    print()


