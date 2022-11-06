from os.path import exists
from json import load

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
        raise Exception("can't find config.json, make sure it is in the same folder, or get a new one on GitHub")
            

def get_result(filepath="main.py"):
    f = open(filepath,'r')
    contents = f.read()
    f.close()
    return contents
    
