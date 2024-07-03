n = int(input("Please Enter a natural number: "))

for row in range(0, n):
    for column in range(0, row + 1):
        print("*", end='')
    print()


