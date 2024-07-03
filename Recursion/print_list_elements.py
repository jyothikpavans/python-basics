def print_list_elements(l, length):
    if l == 0:
        return
    print(list_numbers[length - l])
    print_list_elements(l - 1, length)


list_numbers = [1, 45, 32, 43, 99, 101]
length = len(list_numbers)
print_list_elements(length, length)
