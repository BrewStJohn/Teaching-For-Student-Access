# Where should we start? 
# What types of functions should 
# we have in our program?
# --> When the user enters rooms
# --> Handles user inputs

# Why do we have functions in programs? 
# What are they useful for?
# --> useful for organising code
# --> for code that repeats


# 1) Dictionaries! What for?
# a) Game Map
# for every room in the map
# specify which direction the user has to move in to get to the next room
# EXAMPLE: 
# map['bathroom'] = {'south': 'main'}
# map['main'] = {'north': 'bathroom', 'west': 'living_room', 'east': 'kitchen'}

map = {
    'living_room':{
        'east': 'main'
    },
    'bathroom':{
        'south': 'main'
    },
    'kitchen':{
        'west': 'main'
    },
    'main_room':{
        'north': 'bathroom',
        'west': 'living_room',
        'east': 'kitchen'
    }
}

# b) Descriptions
descriptions = {
    # room: description
}

# c) Player
player = {
    # location: room
    # OPTIONAL inventory: [0, 1, 2]
    # OPTIONAL: Statistics (strength, dexterity, health, etc)
}


# 2) Create a function that will handle user input
# The purpose of this function is to run the game by continuially 
# asking the user for inputs. Depending on what they input, we run
# different parts of the game!

# GENERAL PSUEDOCODE:
# def main():
# --> in a while loop that runs until the game is over,
    # --> get input from user
    # --> make sure its valid
    # --> depending on their input, run a function related 
    # to the input
    # REQUIRED: The user should be able to input 'north, south, east or west'
    # and move to that room.

# HINTS: Python Function, Python While Loops, Python inputs, 
# Python Try/Except

directions = ['n', 's', 'e', 'w']

def print_instructions():
    # pretty print what the user can enter in the console
    # EXAMPLE:
    # Type: 'n', 's', 'w', 'e' to go in that cardinal direction
    # Type: 'look' to figure out which rooms are in what direction
    # Type: 'investigate' to learn more about the room
    # Type: 'help' for a clue

def main():
    while game_over is not False:
        print_instructions()
        user_input = input("What would you like to do?")
        if user_input is in directions