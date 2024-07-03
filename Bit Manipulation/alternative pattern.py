n = int(input("Enter a number: "))
flag = 1
while n > 0:
    bit_value = n % 2
    n = n // 2
    new_bit_value = n % 2
    if bit_value == new_bit_value:
        flag = 0
        print("N0")

if flag == 1:
    print("YES")
