
choice = "-"
while choice != "0":
    if choice in "12345":
        print("You choose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn python")
        print("2:\t Learn java")
        print("3:\t go swimming")
        print("4:\t have dinner")
        print("5:\t go to bed")
        print("0:\t exit")

    choice = input()