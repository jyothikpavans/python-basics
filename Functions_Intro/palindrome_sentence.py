def palindrome_sentence(string):
    return string[::-1] == string


word = input("Please enter a sentence to check: ")
length = len(word)
newStr = ""
for i in range(length):
    if word[i].isalnum():
        newStr += word[i].lower()


if palindrome_sentence(newStr):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
