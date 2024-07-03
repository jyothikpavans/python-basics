binary_number = str(input("Please Enter a string of numbers using 0 and 1: "))
#
# decimal_number = 0
# power_of_two = len(binary_number) - 1
#
# for index in range(0, len(binary_number)):
#     decimal_number += pow(2, power_of_two) * int(binary_number[index])
#     power_of_two -= 1
#
# print(decimal_number)

decimal_number = 0
power_of_two = 0

for index in range(0, len(binary_number))[::-1]:
    decimal_number += pow(2, power_of_two) * int(binary_number[index])
    power_of_two += 1

print(decimal_number)

