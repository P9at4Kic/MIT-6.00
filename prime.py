from math import *

## Generates all primes up to n and shows that the sum of the
## log bass e of the primes smaller than the nth prime is
## approximatly equal to the nth prime.

## Inorder to increase efficiency only odd integers will be
## tested. Integer will only be tested against primes
## smaller than the square root of the integer.

def get_n():
    try:
        n = int(input('Input n to generate the nth primt. \n--> '))
        if n > 0:
            return n
        else:
            print ('Input error please input a positive integer.\n')
            return get_n()
    except ValueError:
        print ('Input error please input an integer.\n')
        return get_n()

def prime():
    n = get_n()
    global primes
    primes = [2]                    # list of primes
    testInt = 3                     # next integer to be tested
    sqrtInt = sqrt(testInt)         # square root of test integer
    sumLog = 0                      # sum of the log of primes < n
    while len(primes) < n:
        for x in primes:
            if testInt%x == 0:      # test if x is a factor
                break
            if x > sqrtInt:                 # If no factor is
                sumLog += log(primes[-1])   # smaller than sqrtInt
                primes.append(testInt)      # add to primes
                break
        testInt +=2                 # next odd testInt
        sqrtInt = sqrt(testInt)
    print (primes[-1])

