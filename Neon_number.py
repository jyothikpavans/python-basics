n = int(input("Please Enter a number: "))
p = n * n
sum_digits = 0
square = p

while p > 0:
    r = p % 10
    sum_digits += r
    p = p // 10

if sum_digits == n:
    print("{0} is a Neon number".format(n))
else:
    print("{0} is not a Neon number".format(n))

