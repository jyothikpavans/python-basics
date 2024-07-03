number = int(input("Please enter a number: "))

sum_numbers = 0
for i in range(1, number):
    if number % i == 0:
        sum_numbers += i

if number != 0 and sum_numbers == number:
    print("{0} is a PERFECT NUMBER".format(number))
else:
    print("{0} is not a PERFECT NUMBER".format(number))








