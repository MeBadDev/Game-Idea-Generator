from initalize import initalize
from json import load
from random import choice
initalize()
settings = {
    'rules/types.txt':[],
    'rules/rules.txt':[],
    'rules/place.txt':[]
            }
generate_count = 0
config_file = open('config.json')
config = load(config_file)
config_file.close()

for value in ['rules/place.txt','rules/rules.txt','rules/types.txt']:
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
    return "A %s where %s %s" % (choice(settings['rules/types.txt']), choice(settings['rules/rules.txt']), choice(settings['rules/place.txt']))


for counts in range(generate_count):
    print(get_idea())

print('\n')

