# This is a program the check if a number is a prime or not.
import math

def is_prime(number):
    if number < 1:
        return False

    for i in range(1, int(math.sqrt(number)), 2):
        if number % i == 0:
            return False
        return True

number = int(input("Enter a number: "))
result = is_prime()
if result:
    print("{} is a prime number".format(number))
else:
    print("{} is not a prime number".format(number))

