def binary_to_decimal(number, decimal_number, count):
    if number == 0:
        return decimal_number
    return binary_to_decimal(number // 10, (decimal_number) + pow(2, count) * (number % 10), count + 1)


n = int(input("Enter a number: "))
count = 0
decimal_number = 0
print(binary_to_decimal(n, count, decimal_number))
