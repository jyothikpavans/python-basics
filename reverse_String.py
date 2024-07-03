word = str(input("Please enter a word: "))

i = 0
j = len(word) - 1
wordList = list(word)
print(wordList)

while i < j:
    c = wordList[i]
    wordList[i] = wordList[j]
    wordList[j] = c

    i += 1
    j -= 1
print(wordList)
reversedString = ""
for i in range(0, len(wordList)):
    reversedString += wordList[i]
print("Reversed String:", reversedString)

# print("reverse of a string is {0}:".format(word))

# sentence = str(input("Please type a Sentence: "))
# reverse_sentence = sentence[::-1]
# print(reverse_sentence)
