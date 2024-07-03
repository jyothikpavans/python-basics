word = str(input("Please Enter a word: "))
unique_string = ""
sentence_dict = {}
for letter in word:
    if letter in sentence_dict:
        sentence_dict[letter] += 1
    else:
        sentence_dict[letter] = 1
        unique_string += letter

print(unique_string)
