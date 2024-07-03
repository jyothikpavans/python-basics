# The concept of Slicing
#         012345678901234
parrot = 'Norwegian Blue'

# The below concept-slicing the last character in [] is upto that character but not including it

print(parrot[0:6])  # Norweg
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])  # Norwegian  ---     We can leave the starting index blank in slicing concept if we want to start from first character
print(parrot[10:14])  # Blue
print(parrot[10:])  # Blue  ----  We can leave the last index blank in slicing concept if we want to End until last character

print(parrot[:6])  # Norweg
print(parrot[6:])  # ian Blue

print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"
