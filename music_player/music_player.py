import tkinter as tk
import pygame

#Initialize pygame
pygame.mixer.init()

#Create the main window
window = tk.Tk()
window.title("Music Player")

#Load the music file
pygame.mixer.music.load('test_song.mp3')