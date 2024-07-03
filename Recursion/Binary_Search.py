def binary_search_recursion(data, low, high, item):
    if low <= high:
        middle = (low + high) // 2
        if data[middle] == item:
            return middle
        elif item < data[middle]:
            return binary_search_recursion(data, low, middle - 1, item)
        else:
            return binary_search_recursion(data, middle + 1, high, item)
    else:
        return -1


nums = [3, 5, 8, 15, 26, 38, 47, 136]
print(binary_search_recursion(nums, 0, len(nums) - 1, 136))

