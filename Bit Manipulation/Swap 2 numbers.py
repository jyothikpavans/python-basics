a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

# swapping two numbers using XOR bit - wise operator.
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
