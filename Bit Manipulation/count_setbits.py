def count_set_bits(number, count_setbits):
    if number == 0:
        return count_setbits
    elif number != 0 and (number % 2 == 1):
        count_setbits += 1
    return count_set_bits(number // 2, count_setbits)


n = int(input("Enter a number: "))
count_setbits = 0
print(count_set_bits(n, count_setbits))

