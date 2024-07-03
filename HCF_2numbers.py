#  Q) Write a python Program to Find HCF of Two Numbers.

p = int(input("Please Enter a number: "))
q = int(input("Please Enter another number: "))

n = min(p, q)

while True:
    if p % n == 0 and q % n == 0:
        print(n)
        break
    else:
        n -= 1
