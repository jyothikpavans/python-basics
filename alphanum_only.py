sentence = str(input("Please type a sentence: "))
new_sentence = ''

for letters_numbers in sentence:
    if letters_numbers.isalnum():
        new_sentence += letters_numbers

print(new_sentence)














