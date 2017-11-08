import random


print ('\n' * 50)
print ('You wake in a blood-spattered room. You need to look around to get'
        '\nyour bearings. You need to find out what happened.')

mirror1 = False
mirror2 = False
b_room = False
k_room = False
look_around = False
l_room = False
silence = False
lady = False
keys = False


lroom_intro = ('\nYou are in the living room. There is a kitchen is to the west.'
                '\nThere is a bedroom to the east. The front door is to the '
                'north.\nThere is a window to the south.')


def living_room():
    print lroom_intro
    while True:
        choice = raw_input('\n> ').lower()
        global b_room
        global f_door
        global k_room
        global l_room
        global look_around
        global mirror1
        global mirror2
        global lady
        global talk
        global keys
        if ('search' in choice and 'room' in choice) or ('look around' in choice
        ) and (not k_room and not b_room and not f_door):
            print ('\nThere is a coffee table on its side & a broken mirror on'
                    '\nthe wall.')
            mirror1 = True
        elif ('look' in choice and 'window' in choice) and (not f_door and not
        k_room and not b_room):
            print ('\nYou look out the window to see that it is snowing. You are '
                    '\na few stories up. There is a parking lot below with '
                    '\nthree cars parked in it.')
        elif ('look' in choice) and ('mirror' in choice) and (mirror1 and not
        k_room and not b_room and not f_door):
            print ('\nYou look in the broken mirror to see that your forehead'
                    '\nis bleeding.')
            mirror2 = True # Makes sure user identifies who they are before continuing the game
        elif ('bedroom' in choice or 'go east' in choice) and (not k_room and
        not b_room and not f_door and not lady):
            bedroom()
        elif ('bedroom' in choice or 'go east' in choice) and (lady and not
        k_room and not b_room and not f_door):
            bedroom_lady()
        elif (('go' in choice and 'kitchen' in choice) or ('go' in choice and
        'west' in choice)) and (not k_room and not b_room and not f_door):
            kitchen()
        elif ('go' in choice and 'front door' in choice) or (
        'exit the apartment' in choice) and (not b_room and not k_room and not
        f_door):
            front_door()
        else:
            print ('\nTry again.')


def kitchen():
    global k_room
    print ('\nYou are in the kitchen.')
    k_room = True
    while True:
        choice = raw_input('\n> ').lower()
        global look_around
        if ('go back' in choice) or ('go' in choice and 'living room' in choice
        ) and (k_room):
            k_room = False
            living_room()
        elif (('look around' in choice) or ('search' in choice and 'kitchen' in
        choice)) and (k_room):
            print ('\nThere is a bloody handprint on a drawer. On the counter,'
                    '\nthere is a photograph of a couple in front of a blue car'
                    '\nand a knife block with one knife missing.')
            look_around = True
        elif ('open' in choice and 'drawer' in choice) and (look_around and
        k_room):
            print ('\nYou open the drawer and find a message carved into the wood: '
                    '\n\n\t    H A P P Y'
                    '\n\tH A L L O W E E N')
        else:
            print ('\nTry again.')


def bedroom():
    global b_room
    global lady
    print ('\nYou enter the bedroom. There is a woman handcuffed to the bedpost.'
            '\nShe is still breathing, but barely.')
    b_room = True
    lady = True
    talk = False
    while True:
        choice = raw_input('\n> ').lower()
        global l_room
        global keys
        if ('go' in choice and 'living room' in choice) and (b_room):
            print ('\nYou hear the woman\'s last breath exit her body as you '
                    'leave.')
            l_room = True
            b_room = False
            living_room()
        elif ('talk' in choice and b_room):
            print ('\nYou kneel down next to the woman and ask if she is '
                    'alright.\nShe looks you in the eye and, using all her '
                    'strength,\nsays, "Take my keys. Run."')
            talk = True
        elif ('search' in choice and 'woman' in choice) and (talk):
            print ('\nYou search the woman\'s pockets and find car keys.')
            keys = True
        elif ('take' in choice and 'keys' in choice) and (talk):
            print ('\nYou take the woman\'s car keys.')
            keys = True
        else:
            print ('\nTry again.')


def bedroom_lady():
    global b_room
    print ('\nYou enter the bedroom. The woman is dead.')
    b_room = True
    while True:
        choice = raw_input('\n> ').lower()
        global l_room
        global keys
        if ('go' in choice and 'living room' in choice) and (b_room):
            l_room = True
            b_room = False
            living_room()
        elif ('search' in choice and 'woman' in choice) and (b_room):
            print ('\nYou search the woman\'s corpse and find car keys in her '
                    '\npocket.')
            keys = True
        else:
            print ('\nTry again.')


def front_door():
    global f_door
    print ('\nYou are outside of the apartment. To the east are \nother '
    'apartments. To the west is the elevator.')
    f_door = True
    while True:
        choice = raw_input('\n> ').lower()
        if ('go' in choice and 'east' in choice) and (f_door):
            print ('\nYou walk to the east to discover that there are more '
                    'apartments.\nI just told you that, Genius.')
        elif (('go' in choice and 'west' in choice) or ('go' in choice and
        'elevator' in choice)) and (f_door):
            print ('\nYou enter the elevator. You are on the 5th floor. There '
                    '\nare 8 floors, including a basement level.')
            elevator()
            f_door = False
        elif (('go' in choice and 'back' in choice) or ('go' in choice and
        'inside' in choice) or ('go' in choice and 'apartment' in choice)) and (
        f_door):
            f_door = False
            living_room()
        else:
            print ('\nTry again.')


def elevator():
    while True:
        choice = raw_input('\n> ').lower()
        if ('go' in choice and 'basement' in choice):
            ran_el_basement()
        elif ('go' in choice and 'ground' in choice) or ('go' in choice and '1' in
        choice) or ('go' in choice and '1st' in choice) or ('go' in choice and
        'first' in choice):
            ground_level()
        elif ('go' in choice and '2nd' in choice) or ('go' in choice and 'second' in
        choice) or ('go' in choice and '2' in choice):
            ran_el_level2()
        elif ('go' in choice and '3rd' in choice) or ('go' in choice and 'third' in
        choice) or ('go' in choice and '3' in choice):
            ran_el_level3()
        elif ('go' in choice and '4th' in choice) or ('go' in choice and 'fourth' in
        choice) or ('go' in choice and '4' in choice):
            ran_el_level4()
        elif ('go' in choice and '5th' in choice) or ('go' in choice and 'fifth' in
        choice) or ('go' in choice and '5' in choice):
            print ('\nThe elevator ding and the doors open.')
            front_door()
        elif ('go' in choice and '6th' in choice) or ('go' in choice and 'sixth' in
        choice) or ('go' in choice and '6' in choice):
            ran_el_level6()
        elif ('go' in choice and '7th' in choice) or ('go' in choice and 'seventh' in
        choice) or ('go' in choice and '7' in choice):
            ran_el_level7()
        else:
            print ('\nTry again.')


a = ('\nThe elevator dings as the doors spread. Horror fills you, as you see'
    '\nthe mask. That terrible mask. Michael lumbers towards you. You'
    '\nfrantically tap the \"DOOR CLOSE\" button, but it is no use. Michael'
    '\ngrips your throat and plunges a kitchen knife through your skull.'
    '\nYou have died.')

b = ('\nThe elevator dings as the doors spread. There doesn\'t seem to be'
    '\nanything here.')

c = ('\nThe elevator dings as the doors spread. There doesn\'t seem to be'
    '\nanything here.')

d = ('\nThe elevator dings as the doors spread. A small child is standing with'
    '\nher back to you in the hallway. She turns to look at you. Her throat is'
    '\nslit and she mouths the words, "Help me."'
    '\nYou rub your eyes and she has disappeared. You need to get out of here.')

michael1 = [a, b, c, d]


c1 = ('\nThe elevator door creeks open and the ding carries through your ears'
    '\nslowly, as if in slow motion. Random strobes of light illuminate the'
    '\nhallway before you and you can vaguely make out a flurry of six-legged'
    '\ncreatures crawling the walls. Your skin feels heavy, as though it is'
    '\ndripping off your meat and bones. You black out. Waking in a hospital,'
    '\nyou realize you\'re chained to your bed as a doctor holding a clipboard'
    '\nexplains that you nearly died due to exhaustion. You begin to thank'
    '\nthe doctor, but as you do, his face changes shape. It\'s Michael!'
    '\nHe stabs you repeatedly and you die.')

c2 = ('\nThe elevator dings as the doors spread. Yellow lights flicker in '
    'the \nhallway and you see droves of transluscent women dancing with one \n'
    'another. Looking closer, you realize they are all ghosts of your mother, '
    '\neach from a different time of her life. You need to get out of here.')

c3 = ('\nThe elevator dings as the doors spread. Yellow lights flicker in '
    'the \nhallway and you see droves of transluscent women dancing with one \n'
    'another. Looking closer, you realize they are all ghosts of your mother, '
    '\neach from a different time of her life. You need to get some sleep.')

c4 = ('\nThere doesn\'t seem to be anything here.')

ghosts = [c1, c2, c3, c4]


def ran_el_basement():
    base_chance = (random.choice(ghosts))
    print base_chance
    if ('Michael' in base_chance):
        quit(0)
    else:
        elevator()


def ground_level():
    print ('\nYou have made it to the ground level.'
    '\nTo the north, there is a forest. To the west, there is two feet of snow,'
    '\nall the way to the edge of the apartment complex. To the east, there is'
    '\na shoveled path, leading around the building. To the south, there is the '
    '\nbrick wall of the apartment building.')
    while True:
        choice = raw_input('\n> ').lower()
        if ('go north' in choice) or ('go' in choice and 'forest' in choice):
            print ('\nYou wander through the forest for a few hours, but are '
            'eventually \ntaken by the cold. You die of hypothermia. Your body '
            'isn\'t found \nuntil summer, due to the blizzard of snow creating '
            'a shallow and \nshort-lived resting place for you.')
            quit(0)
        elif ('go' in choice and 'east' in choice) or ('shoveled path' in choice):
            e_side1()
        elif ('go' in choice and 'west' in choice):
            w_side1()
        elif ('go' in choice and 'south' in choice):
            print ('\nThere\'s a brick wall there. You can\'t walk through walls.')
        else:
            print ('\nTry again.')


a1 = ('\nMichael hears the crunch of your boots in the snow and turns to see '
    '\nyou. He lumbers towards you, with his hands outstretched. You turn to '
    '\nrun, but trip and fall into the snow. Michael straddles you and '
    '\nstrangles you to death. You lose.')

a2 = ('\nThe path continues around the building, so you continue to follow it '
    'to \nthe south side of the complex.')

a3 = ('\nThe path continues around the building, so you continue to follow it '
    'to \nthe south side of the complex.')

a4 = ('\nThe path continues around the building, so you continue to follow it '
    'to \nthe south side of the complex.')

a5 = ('\nThe path continues around the building, so you continue to follow it '
    'to \nthe south side of the complex.')

michael2 = [a1, a2, a3, a4, a5]


b1 = ('\nMichael hears the crunch of your boots in the snow and turns to see '
    '\nyou. He lumbers towards you, with his hands outstretched. You turn to '
    '\nrun, but trip and fall into the snow. Michael straddles you and '
    '\nstrangles you to death. You lose.')

b2 = ('\nThe west side of the building looks clear, so you trudge through to snow '
    '\nto the south side of the complex.')

b3 = ('\nThe west side of the building looks clear, so you trudge through to snow '
    '\nto the south side of the complex.')

b4 = ('\nThe west side of the building looks clear, so you trudge through to snow '
    '\nto the south side of the complex.')

b5 = ('\nThe west side of the building looks clear, so you trudge through to snow '
    '\nto the south side of the complex.')

michael3 = [b1, b2, b3, b4, b5]


def e_side1(): # if user chooses to go east
    print ('\nYou hurriedly walk along the path and turn the corner of the '
            'apartment complex.')
    chance = (random.choice(michael2))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        e_side2()


d1 = ('\nYou sprint towards the blue car and open the door with the dead woman\'s'
    '\nkeys. You frantically turn over the engine. The battery is dead. You '
    '\nswivel your head to look around and see Michael, lumbering out of the fog'
    '\ntowards you. He stabs his knife through the car window and into your '
    '\nskull. You\'re dead.')

d2 = ('\nYou sprint towards the blue car and open the door with the dead woman\'s'
    '\nkeys. You frantically turn over the engine. The car starts up and you'
    '\nspeed out of the parking lot and onto the highway.'
    '\nYou\'re free...for now.')

d3 = ('\nYou sprint towards the blue car and open the door with the dead woman\'s'
    '\nkeys. You frantically turn over the engine. The car starts up and you'
    '\nspeed out of the parking lot and onto the highway.'
    '\nYou\'re free...for now.')

d4 = ('\nYou sprint towards the blue car and open the door with the dead woman\'s'
    '\nkeys. You frantically turn over the engine. The car starts up and you'
    '\nspeed out of the parking lot and onto the highway.'
    '\nYou\'re free...for now.')

d5 = ('\nYou sprint towards the blue car and open the door with the dead woman\'s'
    '\nkeys. You frantically turn over the engine. The car starts up and you'
    '\nspeed out of the parking lot and onto the highway.'
    '\nYou\'re free...for now.')

keys_blue_car = [d1, d2, d3, d4, d5]


e1 = ('\nYou break into the car and the alarm goes off. You frantically look'
    '\naround to see Michael lumbering towards you, the moonlight glinting'
    '\noff the kitchen knife in his hand. You panic and jiggle the door handle,'
    '\nbut it\'s no use. Michael brings the knife down through your skull and'
    '\nyou die.')

e2 = ('\nYou break into the car and drive off into the night. You\'re free...'
    '\nfor now.')

e3 = ('\nYou break into the car, hotwire the engine, and pull out of the parking'
    '\nlot and onto the highway. You look in your rearview mirror and see Michael.'
    '\nHe grips your neck from the back seat and you turn the wheel, sending'
    '\nthe car soaring off the edge of the highway. The car explodes, killing'
    '\nyou both.')

nokeys_cars = [e1, e2, e3]


def e_side2(): # if user isn't caught by michael
    print ('You turn the corner and see a parking lot with 3 cars in it. The '
            '\nclosest car is red. The next farthest car is yellow. The '
            '\nfarthest car is blue. \nWhich do you choose?')
    while True:
        choice = raw_input('\n> ').lower()
        global keys
        if ('blue' in choice) and (keys):
            keys_blue_car_random = (random.choice(keys_blue_car))
            print keys_blue_car_random
            quit(0)
        elif ('yellow' in choice) and (keys):
            print ('\nYou sprint towards the yellow car and try to open the door '
                    'with the dead\nwoman\'s keys. They don\'t work. This must '
                    'not be her car. You hear a\nnoise behind you. You turn to '
                    'see Michael. He stabs you in the skull\nand you die.')
            quit(0)
        elif ('red' in choice) and (keys):
            print ('\nYou sprint towards the red car and try to open the door '
                    'with the dead\nwoman\'s keys. They don\'t work. This must '
                    'not be her car. You hear a\nnoise behind you. You turn to '
                    'see Michael. He stabs you in the skull\nand you die.')
            quit(0)
        elif ('blue' in choice) or ('yellow' in choice) or ('red' in choice
        ) and (not keys):
            nokeys_escape = (random.choice(nokeys_cars))
            print nokeys_escape
            quit(0)
        else:
            print ('\nTry again.')


def w_side1(): # if user chooses to go west
    print ('\nYou trudge through the snow to the west side of the apartment '
            'complex.')
    chance = (random.choice(michael3))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        w_side2()

def w_side2(): # if user isn't caught by michael
    print ('You turn the corner to the south side of the complex '
            'and see a \nparking lot with 3 cars in it. The closest car is '
            'blue. The next \nfarthest car is yellow. The farthest car is red. '
            '\nWhich do you choose?')
    while True:
        choice = raw_input('\n> ').lower()
        global keys
        if ('blue' in choice) and (keys):
            keys_blue_car_random = (random.choice(keys_blue_car))
            print keys_blue_car_random
            quit(0)
        elif ('yellow' in choice) and (keys):
            print ('\nYou sprint towards the yellow car and try to open the door '
                    'with the dead\nwoman\'s keys. They don\'t work. This must '
                    'not be her car. You hear a\nnoise behind you. You turn to '
                    'see Michael. He stabs you in the skull\nand you die.')
            quit(0)
        elif ('red' in choice) and (keys):
            print ('\nYou sprint towards the red car and try to open the door '
                    'with the dead\nwoman\'s keys. They don\'t work. This must '
                    'not be her car. You hear a\nnoise behind you. You turn to '
                    'see Michael. He stabs you in the skull\nand you die.')
            quit(0)
        elif ('blue' in choice) or ('yellow' in choice) or ('red' in choice
        ) and (not keys):
            nokeys_escape = (random.choice(nokeys_cars))
            print nokeys_escape
            quit(0)
        else:
            print ('\nTry again.')


def ran_el_level2():
    chance = (random.choice(michael1))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        elevator()


def ran_el_level3():
    chance = (random.choice(michael1))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        elevator()


def ran_el_level4():
    chance = (random.choice(michael1))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        elevator()


def ran_el_level5():
    chance = (random.choice(michael1))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        elevator()


def ran_el_level6():
    chance = (random.choice(michael1))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        elevator()


def ran_el_level7():
    chance = (random.choice(michael1))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        elevator()


def ran_el_level8():
    chance = (random.choice(michael1))
    print chance
    if ('michael' in chance):
        quit(0)
    else:
        elevator()


living_room()
