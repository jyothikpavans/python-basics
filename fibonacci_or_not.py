# To find whether the number is fibonacci or not.

n = int(input("Please Enter a number: "))


def isFibonacci(n: int) -> int:
    if 0 <= n <= 1:
        return True

    n_minus1, n_minus2 = 1, 0
    result = 1
    while result < n:
        result = n_minus2 + n_minus1
        if result == n:
            return True
        n_minus2 = n_minus1
        n_minus1 = result
    return False


if isFibonacci(n):
    print("{0} is a Fibonacci number. ".format(n))
else:
    print("{0} is not Fibonacci number. ".format(n))
