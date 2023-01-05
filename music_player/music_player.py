import tkinter as tk
import pygame

#Initialize pygame
pygame.mixer.init()

#Create the main window
window = tk.Tk()
window.title("Music Player")

#Load the music file
pygame.mixer.music.load('something_in_me.mp3')

# Create the play button
def play():
  pygame.mixer.music.play()
play_button = tk.Button(window, text="Play", command=play)
play_button.pack()

# Create the pause button
def pause():
  pygame.mixer.music.pause()
pause_button = tk.Button(window, text="Pause", command=pause)
pause_button.pack()

# Create the stop button
def stop():
  pygame.mixer.music.stop()
stop_button = tk.Button(window, text="Stop", command=stop)
stop_button.pack()

# Run the main event loop
window.mainloop() 
