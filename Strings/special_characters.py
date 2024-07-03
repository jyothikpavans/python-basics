sentence = str(input("Please Enter a sentence: "))
if sentence.isalnum():
    print("{0} doesn't contain any special characters.".format(sentence))
else:
    print("{0} contains special characters.".format(sentence))
