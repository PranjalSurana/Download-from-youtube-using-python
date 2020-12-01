import os
from moviepy.editor import *

locn=("Enter the destination : ")
os.chdir(locn)
print(os.getcwd())

for i in os.listdir():
    if '.mp4' in i:
        a=str(i)
        b=a[:-1]+'3'
        print(a)
        au = VideoFileClip(a)
        au.audio.write_audiofile(b)
            
