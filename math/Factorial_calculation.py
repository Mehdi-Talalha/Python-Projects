# this project represent whats going under the hood of the factorial methods of math module

def factorial(n):
    if n < 0:
        print('invalide factorial of a negative number')
    elif n == 0:
        print(1)
    else:
        result = 1
        for i in range(1 , n + 1):
            result *= i
        return result

# get number for the user
n = int(input("Enter a number: "))
print(f"the factorial number of {n} is {factorial(n)}")