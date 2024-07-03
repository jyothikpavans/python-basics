def factorial(n: int):
    p = 1
    for i in range(1, n + 1)[::-1]:
        p *= i
    return p


n = int(input("Please Enter a number: "))
number = n
sum_factorial = 0

while n > 0:
    r = n % 10
    sum_factorial += factorial(r)
    n = n // 10

if sum_factorial == number:
    print("{0} is a peterson number".format(number))
else:
    print("{0} is not a peterson number".format(number))

