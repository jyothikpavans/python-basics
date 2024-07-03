n = int(input("Please Enter a number: "))

if n == 1:
    print(n, "is neither prime nor composite.")
elif n == 2 and n == 3:
    print(n, "is a prime number.")
elif n % 2 == 0:
    print(n, "is not a prime number")
else:
    flag = 1
    for i in range(3, n, 2):
        if n % i == 0:
            print(n, "is not a prime number")
            flag = 0
            break
    if flag == 1:
        print(n, "is a prime number")
    # if isPrime:
    #     print(n, "is a prime number.")
