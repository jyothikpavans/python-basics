numbers = list()
n = int(input("Please Enter how many items you need in the list: "))
sum_items = 0
for i in range(0, n):
    items = int(input("Please enter a number: "))
    numbers.append(items)
    sum_items += items

# print(numbers)
print(sum_items)
average_items = sum_items / n
print(average_items)


