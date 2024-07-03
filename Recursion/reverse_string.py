def reverse_string(l: int):
    if l == -1:
        return
    print(word[l], end='')
    reverse_string(l - 1)


word = str(input("Enter a word: "))
length = len(word)
reverse_string(length - 1)

