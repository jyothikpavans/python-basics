a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
count_flip_bits = 0

while a > 0 and b > 0:
    if a % 2 != b % 2:
        count_flip_bits += 1
    a = a // 2
    b = b // 2

print("No of bits needed to be flipped is", count_flip_bits)

