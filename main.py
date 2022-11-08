from initalize import initalize
from json import load
from random import choice
from reset import reset
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
print(generate_count)
print("""
	  -------------------
	  GAME IDEA GENERATOR
	   (by MeBadDev lol)
	  -------------------
	 """)
def get_idea():
	return "A %s where %s %s" % (choice(settings['rules/types.txt']), choice(settings['rules/rules.txt']), choice(settings['rules/place.txt']))

command = ''
while command != 'quit':
	command = input('enter command, type "help" for help: ')
	print('\n\n\n')
	if command == 'help':
		print("""
			  HELP:
			  reset: replace files that are missing with the one downloaded on github
			  generate: generate game idea
			  quit: quit
			  generate-count [number]: change generate count
			  """)
	elif command == 'generate':
		for i in range(generate_count):
			print(get_idea())
	elif command.startswith('generate-count'):
		count = command.replace('generate-count ','')
		try:
			generate_count = int(count)
		except:
			print('please enter a number!')
	elif command == 'reset':
		reset()
		
	else:
		print('unknown command!')
	print('\n\n\n')