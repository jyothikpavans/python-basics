n = int(input("Enter a positive number: "))
count_no_bits = 0
if n & (n - 1) == 0:
    print(n)
else:
    while n > 0:
        count_no_bits += 1
        n = n // 2
    print(count_no_bits - 1)
    # print(pow(2, count_no_bits - 1))




