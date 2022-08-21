from tkinter import *
from tkvideo import tkvideo
from moviepy.editor import *
from tkinter.filedialog import *
import pygame
from moviepy.editor import *
import moviepy.editor


window = Tk()
window.title("Video_player!")

#------------------open_video-------------------------------------------
video = askopenfilename()
#-----------------------------------------------------------------------
video1 = moviepy.editor.VideoFileClip(video)
audio = video1.audio


audio.write_audiofile("music_video.mp3")
#-----------------------------size video width,height
clip = VideoFileClip(r''+video)
value = clip.size

my_label = Label(window)
my_label.pack(expand=True,fill='both')
#--------------------sound----------------------------------------------
pygame.mixer.init()

pygame.mixer.music.load("music_video.mp3")
pygame.mixer.music.play(loops=0)
#-------------------video-----------------------------------------------
player = tkvideo(video, my_label, loop = 1, size = (value[0],value[1]))


player.play()
#------------------------------------------------------------------------

window.mainloop()