def decimal_to_binary(number):
    if number == 0:
        return 0
    return decimal_to_binary(number // 2) * 10 + number % 2


n = int(input("Enter a number: "))
print(decimal_to_binary(n))
