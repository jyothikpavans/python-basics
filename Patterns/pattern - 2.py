n = int(input("Please Enter a natural number: "))

for row in range(n, 0, -1):
    for column in range(1, row + 1):
        print("*", end='')
    print()
