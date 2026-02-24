import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load a song (change path to your MP3 file)
pygame.mixer.music.load("alarm.mp3")

# Play the song
pygame.mixer.music.play()

# Keep program running (otherwise it closes immediately)
input("Press Enter to stop...")

# Stop the music
pygame.mixer.music.stop()