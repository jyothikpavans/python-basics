# Program to count the number of each vowels

vowels = 'aeiou'
sentence = str(input("Please Enter a sentence: "))

sentence = sentence.casefold()

count = {}.fromkeys(vowels, 0)
for letter in sentence:
    if letter in count:
        count[letter] += 1

print(count)








