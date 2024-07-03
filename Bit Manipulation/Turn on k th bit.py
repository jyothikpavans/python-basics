def turn_on_kth_bit(number, k):
    if k <= 0:
        return number
    return number | (1 << (k - 1))


n = int(input("Enter a number: "))
k = int(input("Enter which bit to be turned on: "))
print(turn_on_kth_bit(n, k))


