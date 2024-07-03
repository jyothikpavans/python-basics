import math

n = int(input("Enter a number: "))
# square_root = math.sqrt(n)
# if square_root == int(n * 1 / pow(n, 1/2)):
#     print("{0} is a perfect square".format(n))
# else:
#     print("{0} is not a perfect square".format(n))

square_root = int(math.sqrt(n))
if square_root * square_root == n:
    print("{0} is a perfect square".format(n))
else:
    print("{0} is not a perfect square".format(n))

