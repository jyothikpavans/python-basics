n = int(input("Please Enter a natural number: "))

for row in range(1, n + 1):
    for column in range(1, n + 1):
        if row == 1 or row == n:
            print("*", end='')
        else:
            if column != 1 and column != n:
                print(" ", end='')
            else:
                print("*", end='')
    print()



