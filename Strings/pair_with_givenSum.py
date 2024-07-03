def string_to_list(str):
    numbers_list = []
    for number in numbers_string.split(" "):
        numbers_list.append(int(number))
    return numbers_list


def pair_sum_nSquare(list):
    for i in range(0, len(numbers_list)):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[i] + numbers_list[j] == x:
                return True
    return False


def pair_sum_nLogN(list):
    list.sort()
    left_index = 0
    right_index = len(numbers_list) - 1
    while left_index < right_index:
        if numbers_list[left_index] + numbers_list[right_index] < x:
            left_index += 1
        elif numbers_list[left_index] + numbers_list[right_index] > x:
            right_index -= 1
        else:
            return True

    return False


def pair_sum_N(list):
    numbers_dict = {}
    for index in range(0, len(numbers_list)):
        if x - numbers_list[index] not in numbers_dict:
            numbers_dict.update({numbers_list[index]: 'true'})
        else:
            return True

    return False


numbers_string = str(input("Please Enter few numbers: "))
numbers_list = string_to_list(numbers_string)
x = int(input("Enter the pair sum to check in list: "))
pair_sum_nLogN(numbers_list)

if pair_sum_N(numbers_list) is True:
    print("Yes! Yes! Yes!")
else:
    print("No! No! No!")
