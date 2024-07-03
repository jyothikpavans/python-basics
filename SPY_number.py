n = int(input("Please Enter a number to check it's SPY or not: "))
number = n
sum_digits = 0
product_digits = 1

while n > 0:
    r = n % 10
    sum_digits += r
    product_digits *= r
    n = n // 10

if sum_digits == product_digits:
    print("{0} is a SPY number".format(number))
else:
    print("{0} is not a SPY number".format(number))






