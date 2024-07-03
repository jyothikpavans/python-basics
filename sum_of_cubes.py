n = int(input("Please enter a number: "))

cube_squares = 0
for i in range(1, n+1):
    cubes = i * i * i
    cube_squares += cubes

print("Sum of Cubes of {0} natural numbers is {1}".format(n, cube_squares))
