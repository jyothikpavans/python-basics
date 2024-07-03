n = int(input("Please Enter a natural number: "))

for row in range(1, n + 1):
    number = 1
    for column in range(1, row + 1):
        print(number, ' ', end='')
        number += 1
    print()

