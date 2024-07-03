def print_xylem_phloem(number: int):
    sum_means = 0
    sum_extremes = 0
    count = 0
    while number > 0:
        remainder = number % 10
        count += 1
        if count == 1 or remainder == number:
            sum_extremes += remainder
        else:
            sum_means += remainder
        number = number // 10

    if sum_extremes == sum_means:
        print("{0} is a Xylem number".format(n))
    else:
        print("{0} is a Phloem number".format(n))


n = int(input("Please Enter a Number: "))
print_xylem_phloem(n)

