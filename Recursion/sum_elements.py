def sum_elements(l) -> int:
    if l == -1:
        return 0
    return list_numbers[l] + sum_elements(l-1)


list_numbers = [1, 45, 32, 43, 99, 101]
sum_numbers = 0
length = len(list_numbers) - 1
print(sum_elements(length))

