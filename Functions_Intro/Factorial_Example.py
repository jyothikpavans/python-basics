def factorial(num: int) -> int:
    """ Return n! (0! is 1)"""
    if num <= 1:
        return 1

    result = 2
    for number in range(3, num + 1):
        result *= number

    return result


for num in range(0, 36):
    print(factorial(num))
