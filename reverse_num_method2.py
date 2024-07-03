number = int(input("Please Enter a number: "))


def no_of_digits(number: int):
    count = 0
    while number > 0:
        r = number % 10
        count += 1
        number = number // 10
    return count


noOfDigits = no_of_digits(number) - 1
reversed_number = 0
while number > 0:
    r = number % 10
    reversed_number += r * pow(10, noOfDigits)
    noOfDigits -= 1
    number = number // 10
print(reversed_number)

