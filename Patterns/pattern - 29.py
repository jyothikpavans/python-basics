n = int(input("Please Enter a natural number: "))
number = 1

# 1
# 3 2
# 4 5 6
# 10 9 8 7
num = 1
for row in range(1, n + 1):
    for column in range(1, row + 1):
        if row % 2 != 0:
            if column == 1:
                num += row - 1
            print(num, ' ', end='')
            if column != row:
                num += 1
        else:
            if column == 1:
                num += row
                print(num, ' ', end='')
            else:
                num -= 1
                print(num, ' ', end='')
    print()
