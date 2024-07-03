def string_palindrome(l, start_point):
    if string[start_point] != string[l]:
        return False
    if start_point >= l and string[start_point] == string[l]:
        return True
    return string_palindrome(l - 1, start_point + 1)


string = str(input("Enter a word: "))
length = len(string)
start_point = 0
print(string_palindrome(length - 1, start_point))

