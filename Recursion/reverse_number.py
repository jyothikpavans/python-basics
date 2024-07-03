def reverse_number(number, reversed_number) -> int:
    if number == 0:
        return reversed_number
    reversed_number = (reversed_number * 10) + number % 10
    return reverse_number(number // 10, reversed_number)


n = int(input("Enter a number: "))
reversed_number = 0
print(reverse_number(n, reversed_number))
if reverse_number(n, reversed_number) == n:
    print("Palindrome")
else:
    print("Not Palindrome")
