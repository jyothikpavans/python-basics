def max_element(l, max) -> int:
    if l == - 1:
        return max
    if list_numbers[l] > max:
        max = list_numbers[l]
    return max_element(l - 1, max)


list_numbers = [1, 45, 32, 43, 99, 101, 35, 85]
length = len(list_numbers)
maximum = list_numbers[0]
print(max_element(length - 1, maximum))


def min_element(l, min) -> int:
    if l == -1:
        return min
    if list_numbers[l] < min:
        min = list_numbers[l]
    return min_element(l - 1, min)


list_numbers = [48, 10, 93, 1, 45, 32, 43, 99, 101, 35, 85]
length = len(list_numbers)
minimum = list_numbers[0]
print(min_element(length - 1, minimum))
