name = input("Please Enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

#if age >= 18:
 #   print("you are old enough to vote")
  #  print("please put an X in the box")
#else:
    #print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, yoda, you die in the return of the jedi")
else:
    print("you are old enough to vote")
    print("please put an X in the box")
