n = int(input("Please enter a positive number: "))
t = input("Please enter text: ")


def sum_eo(n, t):
    if t == 'e':
        sum_even = 0
        for i in range(2, n, 2):
            sum_even += i
        return sum_even

    elif t == 'o':
        sum_odd = 0
        for j in range(1, n, 2):
            sum_odd += j
        return sum_odd

    elif t != 'e' or t != 'o':
        return -1


print(sum_eo(n, t))
