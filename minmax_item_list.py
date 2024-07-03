numbers = list()
n = int(input("Please Enter how many items you need in the list: "))
for i in range(0, n):
    items = int(input("Please enter a number: "))
    numbers.append(items)

# To find the max item in a list.
max_item = numbers[0]

for item in numbers:
    if item > max_item:
        max_item = item

print("Maximum of list:", max_item)
#
# # To find the min item in a list.
min_item = numbers[0]

for index in range(0, len(numbers)):
    if numbers[index] < min_item:
        min_item = numbers[index]

print("Minimum of list:", min_item)
