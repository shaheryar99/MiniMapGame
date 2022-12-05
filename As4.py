import random
import sys

if len(sys.argv) != 2:
	print('Usage: python3', sys.argv[0], 'map-file-name')
	sys.exit()

def loadmap(n):
	MAP = {}
	holder = ''
	INFILE = n
	f = open(INFILE, 'r')
	for line in f:
		line = line.strip()
		if line == 'ROOM':
			line = f.readline()
			coordinates = line.split()
			xcoord = int(coordinates[0])
			ycoord = int(coordinates[1])
			yxcoord = (ycoord,xcoord)
			while True:
				value = f.readline()
				if value == 'END\n':
					break
				else:
					holder = holder + value
				MAP[yxcoord] = holder
		else:
			continue
	f.close()
	return MAP

MAP = loadmap(sys.argv[1])

dark = True
coordinates = list(MAP)
roomx = coordinates[0][1]
roomy = coordinates[0][0]


aliases = {
	'exit':		'quit',
	'exeunt':	'quit',
	'lantern':	'lamp',
	'n':		'north',
	's':		'south',
	'w':		'west',
	'e':		'east',
}

while True:
	if not dark and random.random() < 0.1:
		print('A gust of wind blows out your lamp!')
		dark = True
	if dark:
		print('It is dark.')
	else:
		coord = (roomy, roomx)
		print(MAP[coord])

	try:
		s = input('? ')
	except EOFError:
		break
	except KeyboardInterrupt:
		break

	s = s.strip()
	if s.isupper():
		print("You don't have to yell.  Honestly.")
		s = s.lower()

	# canonicalize the command
	if s in aliases:
		s = aliases[s]

	oldroomx = roomx
	oldroomy = roomy

	if s == 'quit':
		break
	elif s == 'drink':
		print('*hic*')
	elif s == 'eat':
		print('OM NOM NOM NOM COOOOOOKIE!')
	elif s == 'lamp':
		print('You are enlightened.')
		dark = False
	elif s == 'north':
		roomy = roomy - 1
	elif s == 'south':
		roomy = roomy + 1
	elif s == 'west':
		roomx = roomx - 1
	elif s == 'east':
		roomx = roomx + 1
	else:
		print("I don't know that command.")

	if (roomy, roomx) not in MAP:
		print("You can't move that way!")
		roomx = oldroomx
		roomy = oldroomy

print('Goodbye!')