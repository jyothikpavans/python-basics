def no_of_digits(number, count_digits) -> int:
    if number == 0:
        return count_digits
    return no_of_digits(number // 10, count_digits + 1)


def noOfDigits(number) -> int:
    if number == 0:
        return 0
    return 1 + noOfDigits(number // 10)


n = int(input("Enter a number: "))
counter_digits = 0
print(no_of_digits(n, counter_digits))
print(noOfDigits(n))
