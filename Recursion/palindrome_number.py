def reverse_number(number, reversed_number):
    if number == 0:
        return reversed_number
    reversed_number = (reversed_number * 10) + (number % 10)
    return reverse_number(number // 10, reversed_number)


def palindrome(number, reversed_number, original_number):
    if number == 0:
        return reversed_number == original_number
    reversed_number = (reversed_number * 10) + (number % 10)
    return palindrome(number // 10, reversed_number, original_number)


n = int(input("Enter a number: "))
reversed_number = 0
original_number = n
#reverse_number(n, reversed_number)

# if reverse_number(n, reversed_number) == n:
# if palindrome(n, reversed_number, n):
#     print("Palindrome")
# else:
#     print("Not Palindrome")
print(palindrome(n, reversed_number, original_number))
