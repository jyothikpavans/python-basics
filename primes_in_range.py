# Python function to print prime numbers between two given numbers
p = int(input("Please Enter a number: "))
q = int(input("Please Enter a number: "))
# n = int(input("Please Enter a number: "))


def is_prime(n: int):
    if n == 1:
        return False
    elif n > 2 and n % 2 == 0:
        return False
    else:
        flag = 1
        for i in range(3, n, 2):
            if n % i == 0:
                flag = 0
                break
        if flag == 1:
            return True


for n in range(p, q + 1):
    if is_prime(n):
        print(n, end=' ')





