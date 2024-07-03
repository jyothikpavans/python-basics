number = int(input("Enter a number: "))
k = int(input("Enter which bit to be checked whether set or not: "))

if number & (1 << k):
    print("Yes --  bit is set.")
else:
    print("No -- bit is not set.")

