def isArmstrong(number: int):
    sum_cubes = 0
    number = n
    while number > 0:
        revised_number = number % 10
        sum_cubes += revised_number * revised_number * revised_number
        number = number // 10
    return sum_cubes == n


p = int(input("Please Enter a number: "))
q = int(input("Please Enter another number: "))

for n in range(p, q + 1):
    if isArmstrong(n):
        print(n, " is armstrong number")
