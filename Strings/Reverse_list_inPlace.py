def reverse_list(list):
    i = 0
    j = len(list) - 1

    while i < j:
        c = list[i]
        list[i] = list[j]
        list[j] = c

        i += 1
        j -= 1
    return list


splitted_string = str(input("Please Enter list of numbers: ")).split()
list = []

for string in splitted_string:
    list.append(int(string))

print(reverse_list(list))
