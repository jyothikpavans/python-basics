number = int(input("Please Enter a Number: "))


def reverse_number(n: int):
    reversed_number = 0
    while n > 0:
        r = n % 10
        reversed_number = (reversed_number * 10) + r
        n = n // 10
    return reversed_number


if number == reverse_number(number):
    print("{0} is a palindrome".format(number))
else:
    print("{0} is not a palindrome".format(number))
