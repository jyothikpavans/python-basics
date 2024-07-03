def reverse_number(n: int):
    reversed_number = 0
    while n > 0:
        r = n % 10
        reversed_number = (reversed_number * 10) + r
        n = n // 10
    return reversed_number


number = int(input("Please Enter a Number: "))
print(reverse_number(number))
