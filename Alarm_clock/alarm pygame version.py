import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load a song (change path to your MP3 file)
pygame.mixer.music.load("alarm.mp3")


while True:
    # take from the user menutes and seconds
    seconds = int(input("Seconds: "))
    menutes = int(input("Menutes: "))

    # convert menites to seconds
    menutes = menutes * 60

    #calculate the total time
    total_time = menutes + seconds

    while total_time > 0:
        time.sleep(1)
        total_time-=1
        print("remaining time ", total_time)

    # Play the song
    pygame.mixer.music.play()
    print("Done")
