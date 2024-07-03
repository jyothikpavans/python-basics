n = int(input("Please Enter a natural number: "))
last_column = 1
for row in range(1, n + 1):
    for column in range(1, n + 1):
        if column in range(1, last_column + 1):
            print("*", end='')
        else:
            print(" ", end='')
    last_column += 1
    print()

last_column = n
for row in range(1, n):
    for column in range(1, n + 1):
        if column in range(1, last_column):
            print("*", end='')
        else:
            print(" ", end='')
    last_column -= 1
    print()
