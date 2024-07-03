n = int(input("Please Enter a natural number: "))

for row in range(1, n + 1):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for column in range(1, row + 1):
        print(letter[row - 1], end='')
    print()
