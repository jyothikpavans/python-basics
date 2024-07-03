sentence = str(input("Please Enter a sentence: ")).split()
reverse_words_string = ""
for i in range(len(sentence) - 1, -1, -1):
    reverse_words_string = reverse_words_string + sentence[i] + " "

print(reverse_words_string)


