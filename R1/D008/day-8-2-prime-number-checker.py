from math import ceil, sqrt

def prime_checker(number):
    n = ceil(sqrt(number))
    while True:
        if number == 2:
            print("This is a prime number")
            return False
        for i in range(n):
            if number % 2 == 0:
                print("This is not a prime number")
                return False
        print("This is a prime number")
        return False

n = int(input("Check this number: "))
prime_checker(number=n)