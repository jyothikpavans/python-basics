#  Q) Write a python Program to Find LCM of Two Numbers.

p = int(input("Please Enter a number: "))
q = int(input("Please Enter another number: "))

n = max(p, q)

while True:
    if n % p == 0 and n % q == 0:
        print(n)
        break
    else:
        n += 1








