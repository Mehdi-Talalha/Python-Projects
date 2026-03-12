import random, time, sys, string

strings = list(char for char in string.printable if char not in set(string.digits) and char not in set(string.punctuation))

try:
    # get the user name
    name = input("Enter Your Name: ")
    # check if the name is valide
    if name == '':
        print("Invalide name")
        sys.exit()

    memory = ''

    for i in name:
        char = None
        while char != i:
            char = random.choice(strings)
            print(memory + char) 
            time.sleep(0.01)
        memory = memory + i

except KeyboardInterrupt:
    sys.exit()