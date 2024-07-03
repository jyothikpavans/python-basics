def secondMax_inList(list):
    maximum = 0
    second_maximum = 0
    for index in range(len(list)):
        if list[index] > maximum:
            second_maximum = maximum
            maximum = list[index]

        if list[index] > second_maximum and list[index] != maximum:
            second_maximum = list[index]

    return second_maximum


splitted_string = str(input("Please Enter list of numbers: ")).split()
list = []
for string in splitted_string:
    list.append(int(string))

print(secondMax_inList(list))
