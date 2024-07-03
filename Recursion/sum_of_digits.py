def sum_digits(number, sum_of_digits) -> int:
    if number == 0:
        return sum_of_digits
    return sum_digits(number // 10, sum_of_digits + number % 10)


def sum_of_digits(number) -> int:
    if number == 0:
        return 0
    return number % 10 + sum_of_digits(number // 10)


n = int(input("Enter a number: "))
sum = 0
print(sum_digits(n, sum))
print(sum_of_digits(n))
