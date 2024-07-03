n = int(input("Please Enter a natural number: "))

previous_column = n
next_column = n
alphabets = "AB"

for row in range(1, n + 1):
    letter = alphabets[0]
    for column in range(1, 2 * n):
        if column == previous_column:
            print(letter, end='')
        elif column == next_column:
            print(alphabets[1],end='')
        else:
            print(" ", end='')
    previous_column -= 1
    next_column += 1
    print()

previous_column = 2
next_column = (2 * n) - 2
alphabets = "AB"

for row in range(1, n):
    letter = alphabets[0]
    for column in range(1, 2 * n):
        if column == previous_column:
            print(letter, end='')
        elif column == next_column:
            print(alphabets[1], end='')
        else:
            print(" ", end='')
    previous_column += 1
    next_column -= 1
    print()
