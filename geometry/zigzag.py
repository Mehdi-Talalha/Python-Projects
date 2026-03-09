# lets import the needed modules
import sys, time
# creat the global variables
spaces = 0
is_inceasing = True

try:
    while True: # the main loop
        print(' ' * spaces, end="") # this will print the spaces
        print("******") # and this will print the stars
        # stop a while
        time.sleep(0.1)

        # check if it increase 
        if is_inceasing:
            # if its add spcae until it get the max 20
            spaces = spaces + 1
            if spaces == 20:
                is_inceasing = False
        else:
            # the opposet of the last one
            spaces = spaces - 1
            if spaces == 0:
                is_inceasing = True
except KeyboardInterrupt:
    sys.exit()
