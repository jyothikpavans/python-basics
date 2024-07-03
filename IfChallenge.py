name = input("Your good name please: ")
age = int(input("How old are you? "))

if 18 < age < 31:
    print("Welcome to the holiday, {0}".format(name))
else:
    print("Sorry, you are not allowed for holiday")
