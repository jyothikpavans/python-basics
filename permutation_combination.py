def factorial(n: int):
    b = 1
    for i in range(1, n + 1):
         b *= i
    return b


n = int(input("Please enter a number: "))
r = int(input("Please enter another number: "))

npr_permutation = factorial(n) / factorial(n - r)
print(npr_permutation)

ncr_combination = factorial(n) / (factorial(n - r) * factorial(r))
print(ncr_combination)
