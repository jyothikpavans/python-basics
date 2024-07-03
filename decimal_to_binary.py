def decimal_to_binary(number: int):
    binary_number = 0
    count = 0
    while number != 0:
        binary_digit = number % 2
        binary_number += pow(10, count) * binary_digit
        number = number // 2
        count += 1
    return binary_number


n = int(input("Please Enter a number: "))
print(decimal_to_binary(n))



