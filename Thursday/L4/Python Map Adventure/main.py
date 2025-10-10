# 1) Create a dictionary that stores information about our game. Some things to consider:
# a) Rooms
# --> descriptions
# --> Where the user can travel to from said room
# --> i.e. 'living_room': {'west': 'main_room'}
# b) Player
# c) Anything else you can think of

game_map = {
    'main':{
        'east':'kitchen',
        'west': 'living_room', 
        'north': 'bathroom'
    }, 

    'kitchen':{
        'west': 'main'
    }, 

    'living_room':{
        'east': 'main'
    }, 

    'bathroom':{
        'south': 'main'
    }
}

descriptions = {'living_room': 'There is a TV in the middle of the room, displaying nothing but static.',
                'bathroom':'There is a mirror with a knob attached to it.',
                'kitchen':'You find a small safe with a combination lock.', 
                'main': 'Living room to the west, kitchen to the east, bathroom to the north.'
}

player = { 
    'location': 'main'
}

# 2) Create a main game function that runs UNTIL the game is over.
# --> the main game function should continuously ask the user for input.
# HINT: While Loops, Input()