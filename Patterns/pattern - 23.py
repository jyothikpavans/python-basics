n = int(input("Please Enter a odd natural number: "))

first_column = 1
last_column = n

for row in range(1, n + 1):
    for column in range(1, n + 1):
        if column == first_column or column == last_column:
            print("*", end='')
        else:
            print(" ", end='')
    first_column += 1
    last_column -= 1
    print()


