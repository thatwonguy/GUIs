import tkinter as tk
import pygame
import pyaudio
import wave


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

# Initialize pyadio
p = pyaudio.PyAudio()

def record_audio():
  # Open a wave file to write the audio
  audio_file = wave.open('audio.wav', 'wb')
  audio_file.setnchannels(1)
  audio_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
  audio_file.setframerate(44100)

  # Start recording
  stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
  audio_data = stream.read(44100)
  audio_file.writeframes(audio_data)
  stream.stop_stream()
  stream.close()
  audio_file.close()

# Create a function to play audio
def play_audio():
  # Open the wave file
  audio_file = wave.open('audio.wav', 'rb')
  
  # Start playback
  stream = p.open(format=p.get_format_from_width(audio_file.getsampwidth()),
                  channels=audio_file.getnchannels(),
                  rate=audio_file.getframerate(),
                  output=True)
  audio_data = audio_file.readframes(1024)
  while audio_data:
    stream.write(audio_data)
    audio_data = audio_file.readframes(1024)
  stream.stop_stream()
  stream.close()
  audio_file.close()

# Create a record button
record_button = tk.Button(window, text="Record", command=record_audio)
record_button.pack(expand=1,fill=tk.BOTH)

# Create a play button
play_recording = tk.Button(window, text="Play Recording", command=play_audio)
play_recording.pack(expand=1,fill=tk.BOTH)

# Run the main event loop
window.mainloop() 