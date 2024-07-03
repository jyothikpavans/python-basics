# Python Program to print n Odd/Even Fibonacci numbers if n is given.
n = int(input("Please Enter your Number: "))


def n_odd_even_fibonacci(n: int) -> int:
    """Python Program to print n Odd/Even Fibonacci numbers if n is given."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    count = 0
    while True:
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
        if result % 2 == 0:
            print(result, end=' ')
            count += 1
            if count == n:
                break


n_odd_even_fibonacci(n)

print("are the first {0} Even fibonacci numbers".format(n))

