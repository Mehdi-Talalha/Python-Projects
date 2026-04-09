def convert_to_base_10(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

base_2_number = int(input("Enter a number in base 2: "))
base_10_number = convert_to_base_10(base_2_number)
print("Your number {} become {} in base 10".format(base_2_number, base_10_number))