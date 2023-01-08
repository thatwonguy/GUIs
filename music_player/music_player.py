import tkinter as tk
import pygame

#Initialize pygame
pygame.mixer.init()

#This will open up a pygame display window when program is run
# pygame.display.set_mode((400, 300)) 

#Create the main window
window = tk.Tk()

#Set the size of the window
window.geometry('600x300')

#All window to be resizable by user
window.resizable(True,True)

#Set title of GUI window
window.title("Music Player")

#Load the music file
pygame.mixer.music.load('music.mp3')

# Create the play button
def play():
  pygame.mixer.music.play()
play_button = tk.Button(window, text="Play", command=play)
play_button.pack(expand=1,fill=tk.BOTH)
# play_button.place(x=0,y=0)

# Create the fade out button
def fadeout():
  pygame.mixer.music.fadeout(3000)
fadeout_button = tk.Button(window, text="Fade Out", command=fadeout)
fadeout_button.pack(expand=1,fill=tk.BOTH)
# fadeout_button.place(x=320,y=0)

# Create the pause button
def pause():
  pygame.mixer.music.pause()
pause_button = tk.Button(window, text="Pause", command=pause)
pause_button.pack(expand=1,fill=tk.BOTH)
# pause_button.place(x=160,y=0)

# Create the unpause button
def unpause():
  pygame.mixer.music.unpause()
unpause_button = tk.Button(window, text="Unpause", command=unpause)
unpause_button.pack(expand=1,fill=tk.BOTH)
# unpause_button.place(x=240,y=0)

# Create the stop button
def stop():
  pygame.mixer.music.stop()
stop_button = tk.Button(window, text="Stop", command=stop)
stop_button.pack(expand=1,fill=tk.BOTH)
# stop_button.place(x=80,y=0)

# Run the main event loop
window.mainloop() 

