n = int(input("Please Enter a number: "))

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
index = 0
for row in range(n, 0, -1):
    for column in range(1, n + 1):
        letter = alphabets[index]
        if column == row or column > row:
            print(letter, end='')
            index += 1
        else:
            print(' ', end='')
    print()

