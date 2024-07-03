def is_prime(n: int):
    if n == 1:
        return False
    elif n > 2 and n % 2 == 0:
        return False
    else:
        flag = 1
        for i in range(3, n, 2):
            if n % i == 0:
                flag = 0
                break
        if flag == 1:
            return True


def reverseNumber(n: int):
    reverse_number = 0
    while n > 0:
        remainder = n % 10
        reverse_number = (reverse_number * 10) + remainder
        n = n // 10
    return reverse_number


number = int(input("Please Enter a number: "))

if is_prime(number) and is_prime(reverseNumber(number)):
    print("{0} is a Emirp number".format(number))
else:
    print("{0} is not a Emirp number".format(number))

