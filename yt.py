import os
import pathlib
import glob
from pytube import YouTube
from moviepy.editor import *

print("* Downloading videos *\n")
filepath = "links.txt"
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        try:
            YouTube(line).streams.first().download()
        except:
            print("Could not download that video")
        line = fp.readline()
        cnt += 1
       
print("\n* Converting to mp3 *\n")
for file in glob.glob("*.mp4"):
    video = VideoFileClip(file)
    video.audio.write_audiofile("mp3/" + file.replace("mp4","") +".mp3")
    print("Removing " + file)
    os.remove(file)
    
print("\n* Finished *")
