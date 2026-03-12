#  this program will generate a matrix with 0s and 1s
# import the needed modules
import random, sys, time, colorama
from colorama import Fore

colorama.init(autoreset=True)

# set a constant Width
WIDTH = 70

try:
    column = [0] * WIDTH

    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                column[i] = random.randint(4, 14)

            if column[i] == 0:
                print(' ',end='')
            else:
                print(Fore.GREEN +  f"{random.choice([0,1])}", end='')
                column[i] -= 1
        print()
        time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()
