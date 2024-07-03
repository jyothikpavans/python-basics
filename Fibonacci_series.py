# To print Fibonacci series for n numbers


def fibonacci(n: int) -> int:
    """Return the fibonacci numbers below n, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    print(n_minus2, end='')
    result = 1
    while result <= n:
        print('', result, end='')
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result


n = int(input("Enter n: "))
fibonacci(n)
#  0 1 1 2 3 5 8 13 21 34

