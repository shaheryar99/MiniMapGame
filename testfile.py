# Import much needed respiratories

import random
import sys
import re
import itertools

# Defining global variables
dark = True
# roomx = 2
# roomy = 1

# Creating an empty dictionary list named MAP
MAP = {

}

# Defining some commands
aliases = {
    'exit': 'quit',
    'exeunt': 'quit',
    'lantern': 'lamp',
    'n': 'north',
    's': 'south',
    'w': 'west',
    'e': 'east',
}


# Create the function loadmap
def loadmap():
    # Open the file
    filename = ''.join(sys.argv[1:])
    fileto_open = filename
    f = open(fileto_open, 'r')
    room = 0
    alltext = ''
    # Read the lines in the file
    for x in f:
        # nostripx = x
        x = x.strip()
        # If line is ROOM
        if x == "ROOM":
            stringr = str(room)
            global roomr
            roomr = "R" + stringr
            global R0
            coord = f.readline()
            splitcoord = coord.split()
            global initxcord
            global initycord
            xcoord = int(splitcoord[0])
            ycoord = int(splitcoord[1])
            # Used so I can use the value of R0 to define roomx, roomy.
            if roomr == "R0":
                initxcord = xcoord
                initycord = ycoord
                R0 = 1
            # Read the text lines and put them in variable text
            while True:
                text = f.readline()
                # if "END" in text:
                if re.search(r'\bEND\b', text):
                    break
                # Add to map
                else:
                    alltext = alltext + text
                    MAP[ycoord, xcoord] = alltext
                    print("THE TEXT TO PRINT IS:", alltext)
                    #print(MAP)
            # Count R0, R1 etc.
            room = room + 1
        else:
            print("Error! I went looking for the line 'ROOM' and couldn't find it. Instead I found:", x,
                  ".Please recheck your file. This program will exit in 1 second.")
            sys.exit(1)


# If a single map file is supplied:
if len(sys.argv) == 2:
    loadmap()
    # Defining roomx and roomy
    if R0 == 1:
        roomx = initxcord
        roomy = initycord
    while True:
        try:
            # If the lamp is on, at random it may turn off
            if not dark and random.random() < 0.1:
                print('A gust of wind blows out your lamp!')
                dark = True
            if dark:
                print('It is dark.')
            else:
                # Continue to the regular coordinates
                position = (roomy, roomx)
                print(MAP[position])
            # Taking in the input
            s = input('? ')

            s = s.strip()
            # If input is uppercase
            if s.isupper():
                print("You don't have to yell. Honestly.")
                s = s.lower()

            # canonicalize the command
            if s in aliases:
                s = aliases[s]

            oldroomx = roomx
            oldroomy = roomy

            # Using the global commands above and assigning a value to them
            if s == 'quit':
                break
            elif s == 'drink':
                print('*hic*')
            elif s == 'eat':
                print('OM NOM NOM NOM COOOOOOKIE!')
            elif s == 'lamp':
                print('You are enlightened.')
                dark = False
            # Defining directions and their effects on the coordinates
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

            # If the coordinate does not exist (a wall)
            if (roomy, roomx) not in MAP:
                print("You can't move that way!")
                roomx = oldroomx
                roomy = oldroomy
        except EOFError:
            print("You pressed CTRL+D, exiting program.")
            sys.exit(1)
        # CTRL+C input
        except KeyboardInterrupt:
            print("You pressed CTRL+C, exiting program.")
            sys.exit(1)
        # IO Error
        except IOError as io:
            print("I/O error({0}): {1}".format(io.errno, io.strerror))
            sys.exit(1)
        # If anything else happens
        except:
            print("Unexpected error in file:", sys.argv[1:], sys.exc_info()[0])
            sys.exit(1)
    print('Goodbye!')
# If too many map files supplied at once
elif len(sys.argv) > 2:
    print("Too many map files were entered. Please enter one command at a time.")
# If no map files supplied at all
else:
    print("No map files were entered. Please enter a command.")
