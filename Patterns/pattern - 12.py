n = int(input("Please Enter a natural number: "))

for row in range(1, n + 1):
    for column in range(1, n + 1):
        print("*", " ", end='')
    print()
