def print_strontio_not(n: int):
    double_number = n * 2
    count = 0
    while double_number > 0:
        remainder = double_number % 10
        count += 1
        if count == 2:
            tens_digit = remainder
        elif count == 3:
            hundreds_digit = remainder
        double_number = double_number // 10

    if tens_digit == hundreds_digit:
        print("{0} is a strontio number".format(n))
    else:
        print("{0} is not a strontio number".format(n))


n = int(input("Please Enter a Four digit number: "))
print_strontio_not(n)

