def fizz_buzz(n: int) -> str:
    """
    The fizz_buzz function is a game played by just saying numbers.
    But the thing is if the number divisible by 3 we have to say `fizz`
    divisible by 5 we have to say `buzz`and if its divisible by both
     3 and 5 say `fizz buzz`not divisible by 3 or 5
    print the number.
    :param n: We should have set of numbers in this game suppose 1 to 100
    :return: The function should always return a string like fizz or buzz
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


input("Play Fizz buzz.  Press Enter to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))



