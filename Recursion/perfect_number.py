def perfect_number(number, sum_divisors, original_number):
    if number == 0:
        return sum_divisors == original_number
    if original_number % number == 0:
        return perfect_number(number - 1, sum_divisors + number, original_number)
    return perfect_number(number - 1, sum_divisors, original_number)


n = int(input("Enter a number: "))
original_number = n
sum_divisors = 0
print(perfect_number(n - 1, sum_divisors, original_number))
