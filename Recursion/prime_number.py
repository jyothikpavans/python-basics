def prime_number(number, original_number):
    if number == 1:
        return True
    if (original_number % number == 0) or (original_number % 2 == 0 and original_number != 2):
        return False
    return prime_number(number - 1, original_number)


n = int(input("Enter a number: "))
original_number = n
print(prime_number(n - 1, original_number))
