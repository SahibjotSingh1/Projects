import moviepy.editor 
from tkinter.filedialog import *

#Prompts File Explorer and saves video file in video1
video = askopenfilename()
video1 = moviepy.editor.VideoFileClip(video)
#Audio from video1 is stored in audio variable
audio = video1.audio

#Saves the audio file as "sample.mp3"
audio.write_audiofile("sample.mp3")
print("Completed")


