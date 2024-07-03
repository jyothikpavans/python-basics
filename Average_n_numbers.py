n = int(input("Please enter no. of numbers average you want: "))

sum_numbers = 0
for i in range(n):
    number = float(input("Please enter a number: "))
    sum_numbers += number


average_numbers = sum_numbers / n

print(average_numbers)

