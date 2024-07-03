def isPrime(n: int):
    if n == 1:
        return False
    elif n > 2 and n % 2 == 0:
        return False
    else:
        flag = 1
        for i in range(3, n, 2):
            if n % i == 0:
                flag = 0
                break
        if flag == 1:
            return True


# to print n primes if n is given.
def printNPrimes(no_of_primes: int):
    count = 0
    number = 1
    while count < no_of_primes:
        if isPrime(number):
            print(number, end=' ')
            count += 1
        number += 1


# no_of_primes = int(input("Please Enter no of primes to print: "))
# printNPrimes(no_of_primes)

# to print n alternative primes if n is given.
def printNAlternativePrimes(no_of_alternative_primes: int):
    count = 0
    number = 1
    while count < 2 * no_of_alternative_primes:
        if isPrime(number):
            count += 1
            if count % 2 != 0:
                print(number, end=' ')
        number += 1


# no_of_alternative_primes = int(input("Please Enter how many alternative primes to print: "))
# printNAlternativePrimes(no_of_alternative_primes)

# to print nth prime if n is given.
def printNthPrime(nth_prime: int):
    count = 0
    number = 1
    while count != nth_prime:
        if isPrime(number):
            count += 1
            if count == nth_prime:
                print(number, end=' ')
        number += 1


nth_prime = int(input("Please Enter number to find nth prime: "))
printNthPrime(nth_prime)

