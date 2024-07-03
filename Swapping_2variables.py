A = input("Please enter a number for A variable: ")
B = input("Please enter another number for B variable: ")

c = A
A = B
B = c
print("Swapped Value of A variable is {0}, Swapped Value of B variable is {1}"
      .format(A, B))
print(A, B)
