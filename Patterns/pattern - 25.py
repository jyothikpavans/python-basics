n = int(input("Please Enter a natural number: "))

previous_column = n
next_column = n

for row in range(1, n + 1):
    number = 1
    for column in range(1, 2 * n):
        if column in range(previous_column, next_column + 1):
            print(number, end='')
            number += 1
        else:
            print(" ", end='')
    previous_column -= 1
    next_column += 1
    print()


