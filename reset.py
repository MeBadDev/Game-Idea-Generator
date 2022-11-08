from os.path import exists
from requests import get
#RUN THIS FILE TO REDOWNLOAD EVERYTHING MISSING
#YOUR OWN CHANGE WILL GONE!!!
REMOTE_FILE_PATH = {
    "main.py": "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/main.py",
    "config.json": "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/config.json",
    "place.txt" : "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/place.txt",
    "rules.txt" : "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/rules.txt",
    "types.txt" : "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/types.txt",
}


for files in REMOTE_FILE_PATH:
    if not exists(files):
        r = get(REMOTE_FILE_PATH[files]).content
        f = open(files,'w')
        f.write(r.decode())
        f.close()