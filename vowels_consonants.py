word = list(input("Please Enter a Word: "))

vowelCount = 0
consonantCount = 0

for letter in word:
    if letter in "aeiou" and letter.isalpha():
        vowelCount += 1
    elif letter.isalpha():
        consonantCount += 1

print("No. of Vowels in the Word is: ", vowelCount)
print("No. of Consonants in the Word is:", consonantCount)
print("No of special characters in the word is:", len(word) - (consonantCount + vowelCount))
