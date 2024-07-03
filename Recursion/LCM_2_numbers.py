def LCM_2_numbers(a, b, n) -> int:
    if n % a == 0 and n % b == 0:
        return n
    return LCM_2_numbers(a, b, n + 1)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
n = max(a, b)
print(LCM_2_numbers(a, b, n))
