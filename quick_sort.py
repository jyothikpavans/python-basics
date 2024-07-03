def quick_sort(arr, left, right):
    if left < right:
        partition_position = partition(arr, left, right)
        quick_sort(arr, left, partition_position - 1)
        quick_sort(arr, partition_position + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < right and arr[i] < pivot:
        i += 1
    while j > left and arr[j] >= pivot:
        j -= 1

    if i < j:
        arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


