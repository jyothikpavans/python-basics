p = int(input("Please Enter a number: "))
q = int(input("Please Enter another number greater than p: "))


def fibonacci_between_2numbers(p: int, q: int) -> int:
    """ To find the fibonacci numbers in between two given numbers."""
    if 0 <= p and q <= 1:
        return True
    n_minus1, n_minus2 = 1, 0
    while True:
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
        if result > q:
            break
        if p <= result <= q:
            print(result, end=' ')


(fibonacci_between_2numbers(p, q))

