buzz_or_not = int(input("Please Enter a number to check if it's buzz or not: "))

containing_sevenDigit_or_not = buzz_or_not % 10

if (buzz_or_not % 7 == 0 or containing_sevenDigit_or_not == 7) and buzz_or_not != 0:
    print("{0} is a Buzz number".format(buzz_or_not))
else:
    print("{0} is not a Buzz number".format(buzz_or_not))

