def palindrome_or_not(i, string):
    if i >= (len(s))/2:
        return True
    if s[i] != s[len(s) - i - 1]:
        return False
    return palindrome_or_not(i + 1, s)


i = 0
s = str(input("Enter a word: "))
print(palindrome_or_not(i, s))

