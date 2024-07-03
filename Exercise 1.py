letters = "abcdefghijklmnopqrstuvwxyz"

# create a slice that produces the character qpo
backwards = letters[16:13:-1]
print(backwards)

# slice the string to produce edcba
backwards = letters[4::-1]
print(backwards)

# slice the string to produce the last 8 characters in reverse order
backwards = letters[25:17:-1]
print(backwards)

# or another one for last 8 characters in reverse order is
backwards = letters[:-9:-1]
print(backwards)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])
