n = int(input("Please Enter a natural number: "))

for row in range(n, 0, -1):
    for column in range(n, 0, -1):
        if column <= row:
            print("*", end='')
        else:
            print(" ", end='')
    print()

