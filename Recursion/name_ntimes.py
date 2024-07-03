def name(n):
    if n == 0:
        return
    print("Jyothik")
    name(n - 1)
    print("Rohit")


number = int(input("Enter a number: "))
name(number)
