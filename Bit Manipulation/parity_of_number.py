def count_set_bits(number, count_setbits):
    if number == 0:
        return count_setbits
    elif number % 2 == 1:
        count_setbits += 1
    return count_set_bits(number // 2, count_setbits)


n = int(input("Enter a number: "))
set_bits = count_set_bits(n, 0)
if set_bits % 2 == 0:
    print("Even Parity number.")
else:
    print("Odd Parity number.")
