word = str(input("Please type a word: "))

length_word = len(word)
first_character_index = 0
last_character_index = length_word - 1

flag = 1
while first_character_index < last_character_index:
    if word[first_character_index] == word[last_character_index]:
        first_character_index += 1
        last_character_index -= 1
        continue
    else:
        flag = 0
        break

if flag == 1:
    print("The given string is a palindrome. ")
else:
    print(" It's not a palindrome. ")
