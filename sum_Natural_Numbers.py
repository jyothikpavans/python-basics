# Python Program to Find the Sum of Natural Numbers

n = int(input("Please Enter a natural number: "))

sum_numbers = 0
for i in range(1, n + 1):
    sum_numbers += i
print(sum_numbers)
