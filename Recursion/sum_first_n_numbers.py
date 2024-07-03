def sum_n_numbers(n: int) -> int:
    if n == 0:
        return 0
    return n + sum_n_numbers(n - 1)


number = int(input("Enter a number: "))
print(sum_n_numbers(number))

