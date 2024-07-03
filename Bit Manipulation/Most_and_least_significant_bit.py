n = int(input("Enter a number: "))
least_significant_bit = 0

# while n > 0:
#     if n % 2 == 1:
#         break
#     least_significant_bit += 1
#     n = n // 2
#
# print(least_significant_bit)

no_of_bits = 1
while n > 1:
    no_of_bits += 1
    n = n // 2

most_significant_bit = no_of_bits - 1
print(most_significant_bit)

