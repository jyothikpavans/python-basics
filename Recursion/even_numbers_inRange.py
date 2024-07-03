def even_numbers_in_range(a, b):
    if a > b:
        return
    if a % 2 == 0:
        print(a, end=' ')
    return even_numbers_in_range(a + 1, b)


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
even_numbers_in_range(a, b)
