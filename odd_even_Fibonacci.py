# Python Program to print all the Even/Odd Fibonacci numbers below given number - n.

n = int(input("Please Enter a number: "))


def odd_even_fibonacci(n: int) -> int:
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    while True:
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
        if result >= n:
            break
        # if result % 2 == 0:
        #     print(result, end=' ')
        if result % 2 != 0:
            print(result, end=' ')


odd_even_fibonacci(n)

print("are the odd fibonacci numbers below {0}.".format(n))
# print("are the even fibonacci numbers below {0}.".format(n))

