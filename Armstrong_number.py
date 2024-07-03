def armstrong(number: int):
    sum_cubes = 0
    number = n
    while number > 0:
        revised_number = number % 10
        sum_cubes += revised_number * revised_number * revised_number
        number = number // 10
    if sum_cubes == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")


n = int(input("Please Enter a Number: "))
armstrong(n)
