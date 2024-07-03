# Python Program to print a table of a given number

p = int(input("Please Enter a Natural Number: "))

for i in range(1, 11):
    RHS = p * i
    print(p, '*', i, '=', RHS)

