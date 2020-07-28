import os
import pathlib
import glob
import json
from youtube_search import YoutubeSearch
from moviepy.editor import *

def download(line):
    try:
        os.system('youtube-dl "{}" --no-check-certificate'.format(line))
    except:
        print("Could not download that video")
            
def list():
    filepath = "links.txt"
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            download(line)
            line = fp.readline()
            cnt += 1
            
def convert():
    print("\n* Converting to mp3 *\n")
    for file in glob.glob("*.mp4"):
        video = VideoFileClip(file)
        video.audio.write_audiofile("mp3/" + file.replace("mp4","") +".mp3")
        
def remove():
    for file in glob.glob("*.mp4"):
        os.remove(file)       
        
def search():
    print("Keywords")
    sr = input()
    results = YoutubeSearch(sr, max_results=10).to_json()
    print(results)
     
def start():
    print("What do you want to do?\n1. Download & remove mp4 files\n2. Download list.txt\n3. Remove mp4 files\n4. Exit")
    op = input()
    if op == "1":
        list()
        convert()
        remove()
        start()
    if op == "2":
        list()
        convert()
        start()
    if op == "3":
        remove()
        start()
    if op == "4":
        exit()
    
start()
    
print("\n* Finished *")
