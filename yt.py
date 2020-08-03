import os
import pathlib
import glob
import json
from youtube_search import YoutubeSearch
from moviepy.editor import *

numsearch = 1
link = ""
fo = "0"

def download(line):
    try:
        os.system('youtube-dl "{}" --no-check-certificate'.format(line))
        convert('mp4')
        convert('webm')
        convert('mkv')
        remove('mp4')
        remove('webm')
        remove('mkv')
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
            
def names():
    filepath = "names.txt"
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            search(line.strip())
            line = fp.readline()
            cnt += 1
            
def convert(fmt):    
    for file in glob.glob("*."+fmt):
        video = VideoFileClip(file)
        video.audio.write_audiofile("mp3/" + file.replace(fmt,"") +".mp3")
        
def remove(fmt):
    for file in glob.glob("*."+fmt):
        os.remove(file)       

def search(name):
    count = 1
    results = YoutubeSearch(name, max_results=numsearch).to_json()
    data = json.loads(results)
    for videos in data['videos']:
        link = 'https://www.youtube.com'+videos['url_suffix']
        download(link)
        count += 1
        
        
def start():
    print("What do you want to do?\n1. Use links.txt to download mp3\n2. Use names.txt to search and download mp3\n3 NUMBER to set how many found youtube videos download. FX. 3 5 or 3 10\nEnter. to finish\n")
    op = input()
    if op == "1":
        list()
        start()
    if op == "2":
        names()
        start()
    try:
        if op[0] == "3":
            numsearch = op[2:5]
            print("\n* you will download "+op[2:5]+" songs *\n")
            start()
    except:
        sys.exit()
     
if fo == "0":
    start()
    fo = "1"
    
print("* Finished *")
