def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.
    
    The function ignores Whitespace, capitalisation and
    punctuation in the sentence.
    
    :param sentence:  sentence: The sentence to check.
    :return: True if `sentence` is a palindrome. False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence(242)

