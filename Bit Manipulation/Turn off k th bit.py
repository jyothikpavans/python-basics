def turnoff_kth_bit(number, k):
    if k <= 0:
        return number
    return number & ~(1 << (k - 1))


n = int(input("Enter a number: "))
k = int(input("Enter which bit to be turned off: "))
print(turnoff_kth_bit(n, k))
