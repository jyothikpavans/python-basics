string_1 = str(input("Please Enter a string: "))
string_2 = str(input("Please Enter a string: "))
frequency = {}

for letter in string_1:
    if letter not in frequency:
        frequency[letter] = 1
    else:
        frequency[letter] += 1

print(frequency)

flag = 1
for alphabet in string_2:
    if alphabet not in string_1:
        flag = 0
        break
    else:
        frequency[alphabet] -= 1
if flag == 0:
    print("Not Anagram")
else:
    for key in frequency.keys():
        if frequency[key] != 0:
            flag = 0
            break

    if flag == 1:
        print("Anagram.")
    else:
        print("Not Anagram.")
