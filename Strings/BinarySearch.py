def bi_search(list, number):

    binary_search = sorted(list)

    lower_bound = 0
    upper_bound = len(list) - 1

    while lower_bound <= upper_bound:
        mid_index = (lower_bound + upper_bound) // 2

        if list[mid_index] == number:
            return True
        else:
            if list[mid_index] < number:
                lower_bound = mid_index + 1
            else:
                upper_bound = mid_index - 1

    return False


splitted_string = str(input("Please Enter list of few numbers: ")).split()
list = []
for string in splitted_string:
    list.append(int(string))

# print(list)
list.sort()
# print(list)

n = int(input("Please Enter which number to be searched: "))

if bi_search(list, n) is True:
    print("{0} is there in the list".format(n))
else:
    print("{0} is not present in the list".format(n))


