def nth_fibonacci_number(number):
    if number <= 2:
        return number - 1
    return nth_fibonacci_number(number - 1) + nth_fibonacci_number(number - 2)


n = int(input("Enter a number: "))
print(nth_fibonacci_number(n))
