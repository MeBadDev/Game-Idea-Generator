from initalize import initalize
from json import load
from random import choice
initalize()
settings = {
    'types.txt':[],
    'rules.txt':[],
    'place.txt':[]
            }
generate_count = 0
config_file = open('config.json')
config = load(config_file)
config_file.close()

for value in ['place.txt','rules.txt','types.txt']:
    f = open(value)
    contents = f.read().split('\n')
    settings[value].extend(contents)
    f.close()
generate_count = config['generate_count']
print("""
      -------------------
      GAME IDEA GENERATOR
       (by MeBadDev lol)
      -------------------
     """)
def get_idea():
    return "A %s where %s %s" % (choice(settings['types.txt']), choice(settings['rules.txt']), choice(settings['place.txt']))


for counts in range(generate_count):
    print(get_idea())

print('\n')

