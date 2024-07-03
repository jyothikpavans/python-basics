sentence = str(input("Please Enter a sentence: ")).split()

for word in sentence:
    if len(word) % 2 == 0:
        print(word, "", end='')



