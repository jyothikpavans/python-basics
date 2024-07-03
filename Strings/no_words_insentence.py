sentence = str(input("Please Enter a sentence: ")).casefold()

result = sentence.count(" ") + 1
print("The number of words in string are : " + str(result))
