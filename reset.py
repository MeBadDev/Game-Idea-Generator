from os.path import exists
from requests import get
#RUN THIS FILE TO REDOWNLOAD EVERYTHING MISSING
#YOUR OWN CHANGE WILL GONE!!!
REMOTE_FILE_PATH = {
    "initalize.py": "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/initalize.py",
    "README.md": "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/README.md",
    "main.py": "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/main.py",
    "config.json": "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/config.json",
    "rules/place.txt" : "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/rules/place.txt",
    "rules/rules.txt" : "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/rules.txt",
    "rules/types.txt" : "https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/rules/types.txt",
}


for files in REMOTE_FILE_PATH:
    if not exists(files):
        print(f'{files} not found! redownloading...')
        r = get(REMOTE_FILE_PATH[files]).content
        f = open(files,'w+')
        f.write(r.decode().replace('\n',''))
        f.close()
    else:
        print(f'{files}' )