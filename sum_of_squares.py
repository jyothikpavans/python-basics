n = int(input("Please enter a number: "))

sum_squares = 0
for i in range(1, n+1):
    squares = i * i
    sum_squares += squares

print("Sum of Squares of {0} natural numbers is {1}".format(n, sum_squares))

