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

game_over = False
# 2) Create a main game function that runs UNTIL the game is over.
# --> the main game function should continuously ask the user for input.
# HINT: While Loops, Input()

def move_player(input):
    # 3) 
    # store the players location to a local variable
    # for every entry in the map at the players location
        # if that dictionary contains a key that is the same direction as the users input
            # set the players location to that room
            # read out the description of that room
        # otherwise
            # tell the player to input a new direction

def main():
    while game_over is False:
        user_input = input("What would you like to do next? (type \"h\" for help)")
        match user_input:
            # directions
            case "north", "east", "south", "west":
                move_player(user_input)
        # name of item
        # investigate
        # pick up item
            # help
            case "help" | "h":
                print("CONTROLS: \n (h): get information on controls and objective of game")
                print("OBJECTIVE: Escape the mansion alive!")

        # save
        # --> delete save files?
        # chat
        # quit

if __name__ == "__main__":
    main()