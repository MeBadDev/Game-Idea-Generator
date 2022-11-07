from os.path import exists
from json import load
import requests
def initalize():
    if exists('config.json'):
        config_file = open('config.json')
        config = load(config_file)
        config_file.close()
        for path in config['filepaths']:
            path_config = config['filepaths'][path]
            if exists(path_config):
                print(f'{path_config} found!')
            else:
                print(f'{path_config} not found, creating {path_config}...')
                f = open(path_config,'w')
                f.close()

        
        
    else:
        print("no config.json! downloading one from github")
        config_json = requests.get('https://raw.githubusercontent.com/MeBadDev/Game-Idea-Generator/master/config.json')
        f = open('config.json','w')
        f.write(str(config_json.content.decode()))
        f.close()
def get_result(filepath="main.py"):
    f = open(filepath,'r')
    contents = f.read()
    f.close()
    return contents
    

if __name__ == '__main__':
    initalize()