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

descriptions = {
    'living_room': {
        "firstEntry": 'There is a TV in the middle of the room, displaying nothing but static.',
        "gameOver": "The ghost consumes you!"
    },
    'bathroom':'There is a mirror with a knob attached to it.',
    'kitchen':'You find a small safe with a combination lock.', 
    'main': 'Living room to the west, kitchen to the east, bathroom to the north.'
}

player = { 
    'location': 'main'
}

game_over = False

# 3) 
def investigate():
     if player['location'] == 'main':
        question = int(input("You have entered the haunted mansion. There is blah blah blah. What do you want to do? (1) look around (2) leave"))
        if (input == 1):
             print("AAAAAAH")

def move_player(input):
    # store the players location to a local variable
    # for every entry in the map at the players location
    # print(game_map)
        #print(game_map[room].keys().__contains__(input))
        # for available_directions in game_map[player['location']].keys():
        if input in game_map[player['location']].keys():
            player['location'] = game_map[player['location']][input]
        # print(game_map[room].keys())
        else:
             print("You cannot go that direction")
        # if game_map[room].keys
        # if that dictionary contains a key that is the same direction as the users input
            # set the players location to that room
            # read out the description of that room
        # otherwise
            # tell the player to input a new direction

# 2) Create a main game function that runs UNTIL the game is over.
# --> the main game function should continuously ask the user for input.
# HINT: While Loops, Input()
def main():
    while game_over is False:
        beginning()
        user_input = input("What would you like to do next? (type \"h\" for help)")
        match user_input:
            # directions
            case "north" | "east" | "south" | "west":
                move_player(user_input)
        # name of item (use)
        # investigate / interact / chat
            case "investigate":
                investigate()
        # pick up item (grab)
            # help
            case "help" | "h":
                print("CONTROLS: \n (h): get information on controls and objective of game")
                print("OBJECTIVE: Escape the mansion alive!")

        # save
        # --> delete save files?
        # quit

if __name__ == "__main__":
    main()