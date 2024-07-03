# Q) Write a python Program to find sum of digits of a number.

number = int(input("Please Enter a Number: "))
sum_digits = 0
while number > 0:
    revised_number = number % 10
    sum_digits += revised_number
    number = number // 10
print("The sum of digits in the number:", sum_digits)


