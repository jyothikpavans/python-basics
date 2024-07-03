p = int(input("Please Enter a number: "))
q = int(input("Please Enter a number: "))

# r is equal to p power q.
r = 1
for i in range(1, q+1):
     r = r * p
print(r)
