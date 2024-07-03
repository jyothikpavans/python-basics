# def HCF_2_numbers(a, b, n):
#     if a % n == 0 and b % n == 0:
#         return n
#     return HCF_2_numbers(a, b, n - 1)
#
#
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# n = min(a, b)
# print(HCF_2_numbers(a, b, n))


def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


first = 23
second = 69

print('HCF of', first, 'and', second, 'is', hcf(first, second))