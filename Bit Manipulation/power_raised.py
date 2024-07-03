import math


def count_bits(number, count_no_bits):
    if number == 0:
        return count_no_bits
    return count_bits(number // 2, count_no_bits + 1)


n = int(input("Enter a number which is power of 2: "))
count_no_bits = 0
print(count_bits(n, count_no_bits) - 1)