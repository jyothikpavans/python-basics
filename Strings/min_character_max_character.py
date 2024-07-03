sentence = str(input("Please Enter a sentence: "))
letters_dict = {}.fromkeys(sentence, 0)

for letter in sentence:
    letters_dict[letter] += 1

max_value = 0
# min_value = 1
keys = letters_dict.keys()
for letter in keys:
    if letters_dict[letter] > max_value:
        max_character_list = []
        max_value = letters_dict[letter]
        max_character_list.append(letter)
    elif letters_dict[letter] == max_value:
        max_character_list.append(letter)

print(max_character_list, "repeated in the string max no. of times.")

even_frequency_list = []
odd_frequency_list = []

for letter in keys:
    if letters_dict[letter] % 2 == 0:
        even_frequency_list.append(letter)
    else:
        odd_frequency_list.append(letter)

print(even_frequency_list, "has even frequency.")
print(odd_frequency_list, "has odd frequency.")
