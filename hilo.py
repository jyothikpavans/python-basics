low = 1
high = 1000

print("Please think of a number between {} and {}".format(low,high))
input("Please enter to start")

guesses = 1
while low != high:
    #print("\t guessing in the range of {} to {}".format(low,high))
    guess = low + (high-low)// 2
    high_low = input("My guess is {}.should I guess high or lower?"
                     "Enter h or l,or c if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
         # guess higher. THe low end of the range becomes 1 greater than the guess
         low = guess + 1
    elif high_low == "l":
        # guess lower. The high end of the range becomes 1 lesser than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h,l or c")

    # guesses = guesses + 1
    guesses += 1
else:
    print("you thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))

