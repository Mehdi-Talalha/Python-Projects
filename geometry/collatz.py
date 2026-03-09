def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Please type an interger value")
    exit()

result = [number]

while number != 1:
    number = collatz(number)
    result.append(number)

print(result)