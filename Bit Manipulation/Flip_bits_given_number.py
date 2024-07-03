n = int(input("Enter a number: "))
flipped_decimal_number = 0
k = 0

while n >= 1:
    flipped_decimal_number += pow(2, k) * (1 ^ (n % 2))
    k += 1
    n = n // 2

print(flipped_decimal_number)
