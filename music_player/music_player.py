import tkinter as tk
import pygame

#Initialize pygame
pygame.mixer.init()

pygame.display.set_mode((400, 300))

#Create the main window
window = tk.Tk()
window.title("Music Player")

#Load the music file
pygame.mixer.music.load('music.mp3')

# Create the play button
def play():
  pygame.mixer.music.play()
play_button = tk.Button(window, text="Play", command=play)
play_button.pack()

# Create the fade out button
def fadeout():
  pygame.mixer.music.fadeout(3000)
fadeout_button = tk.Button(window, text="Fade Out", command=fadeout)
fadeout_button.pack()

# Create the pause button
def pause():
  pygame.mixer.music.pause()
pause_button = tk.Button(window, text="Pause", command=pause)
pause_button.pack()

# Create the unpause button
def unpause():
  pygame.mixer.music.unpause()
unpause_button = tk.Button(window, text="Unpause", command=unpause)
unpause_button.pack()

# Create the stop button
def stop():
  pygame.mixer.music.stop()
stop_button = tk.Button(window, text="Stop", command=stop)
stop_button.pack()

# Run the main event loop
window.mainloop() 

################## quick and dirty pygame music player test
# import pygame

# # Initialize pygame
# pygame.init()

# # Load the MP3 file
# pygame.mixer.music.load('music.mp3')

# # Play the MP3 file
# pygame.mixer.music.play()

# # Run the main event loop to keep the program running until the song finishes
# while pygame.mixer.music.get_busy():
#   pygame.time.Clock().tick(10)
# test