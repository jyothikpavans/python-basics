def factorial_of_number(n) -> int:
    if n == 1:
        return 1
    return n * factorial_of_number(n - 1)


number = int(input("Enter a number: "))
print(factorial_of_number(number))
