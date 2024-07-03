def bubble_sort(list):
    for number in range(len(list) - 1, 0, -1):
        for index in range(number):
            if list[index] < list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp

    return list


splitted_string = str(input("Please Enter a list of numbers: ")).split()
list = []

for string in splitted_string:
    list.append(int(string))

print(bubble_sort(list))
