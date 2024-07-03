def factorial(n: int):
    r = 1
    for i in range(1, n + 1):
         r *= i
    return r


n = int(input("Please enter a number: "))
print(factorial(n))

