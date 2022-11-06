from initalize import initalize
from json import load
from random import choice
initalize()
settings = {
    'types':[],
    'rules':[],
    'place':[]
            }
generate_count = 0
config_file = open('config.json')
config = load(config_file)
config_file.close()

for keys in config['filepaths']:
    value = config['filepaths'][keys]
    f = open(value)
    contents = f.read().split('\n')
    settings[keys].extend(contents)
    f.close()
generate_count = config['generate_count']
print("""
      -------------------
      GAME IDEA GENERATOR
       (by MeBadDev lol)
      -------------------
     """)
def get_idea():
    return "A %s where %s %s" % (choice(settings['types']), choice(settings['rules']), choice(settings['place']))


for counts in range(generate_count):
    print(get_idea())

print('\n')

