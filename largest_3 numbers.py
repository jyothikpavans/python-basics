number_1 = float(input("Please enter a number: "))
number_2 = float(input("Please enter a number: "))
number_3 = float(input("Please enter a number: "))

if number_1 >= number_2:
    if number_1 >= number_3:
        print("{0} is largest of three numbers".format(number_1))
    else:
        print("{0} is largest of three numbers".format(number_3))
else:
    if number_2 >= number_3:
        print("{0} is largest of three numbers".format(number_2))
    else:
        print("{0} is largest of three numbers".format(number_3))
