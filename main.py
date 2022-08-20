'''
from tkinter import *
from tkvideo import tkvideo

root = Tk()
my_label = Label(root)
my_label.pack()
player = tkvideo("1.mp4", my_label, loop = 1, size = (1280,720))
player.play()

root.mainloop()
'''

from moviepy.editor import *


clip = VideoFileClip(r'1.mp4')

value = clip.size

print("clip size ", end = " : ")
print(value)