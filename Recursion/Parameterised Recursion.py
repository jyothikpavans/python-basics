def parameterised_recursion(n: int):
    if n == 0:
        return 0
    return n + parameterised_recursion(n - 1)


number = int(input("Enter a number: "))
print(parameterised_recursion(number))
