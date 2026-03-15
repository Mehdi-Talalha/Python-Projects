def box_print(symbol, width, height):
    # check the parametter
    if len(symbol) != 1:
        raise Exception("Invalide Length")
    elif width <= 2:
        raise Exception("Width Should be greater than 2")
    elif height <= 2:
        raise Exception("Height should be greater than 2")
    
    # print the box
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# takes from user box preperties
symbol = input("Enter a Charachter: ")
width = int(input("Enter the length of your box: "))
height = int(input("Enter the Height of your box: "))

try:
    box_print(symbol, width, height)
except Exception as err:
    print("Invalude parameter: " + str(err))