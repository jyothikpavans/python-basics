big_word = str(input("Please Enter a word: "))

alphabets = "abcdefghijklmnopqrstuvwxyz"

flag = 1
for alphabet in alphabets:
    if alphabet not in big_word:
        flag = 0
        break

if flag == 1:
    print("Pangram")
else:
    print("Not Pangram")
