def bubble_sort(list):
    for n in range(len(list) - 1, 0, -1):
        for index in range(n):
            if list[index] < list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp

    return list


number_string = str(input("Please Enter a distinct list of numbers: "))
list_numbers = []
for number in number_string.split(" "):
    list_numbers.append(int(number))

print("K value should not be greater than length of list_numbers.")
k = int(input("Enter k value for K th Maximum: "))

print(bubble_sort(list_numbers)[k - 1])



