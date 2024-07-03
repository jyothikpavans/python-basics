def power_a_b(a, b) -> int:
    if b == 1:
        return a
    return a * power_a_b(a, b - 1)


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(power_a_b(a, b))

