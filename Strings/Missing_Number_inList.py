n = int(input("Enter a natural number: "))

input_string = str(input("Enter a list of numbers: "))
list = []
for number in input_string.split(" "):
    list.append(int(number))

index = 0
sum_elements = 0
for index in range(len(list)):
    sum_elements += list[index]
    index += 1

missing_number = (n * (n + 1) / 2) - sum_elements
print(missing_number)
