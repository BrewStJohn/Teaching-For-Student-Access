# 1) Global variables
# --> Storing information

# OTHER THINGS: 
# a) Player dictionary:
# location, inventory, stats

# b) Descriptions
# EXAMPLE
# descriptions = {
#     "livingRoom":{
#         "endGame": "asdSDsd",
#         "firstEnter": "bladhavsdyavsd"
#     },
#     "gameOver": "asdaSDSWD",
# }


game_over = False
map = {
    "livingRoom":{
        "west": "mainRoom"
    },
    "bathroom":{
        "south":"mainRoom"
    },
    "kitchen": {
        "west": "mainRoom",
        "south": "garage"
    },
    "mainRoom":{
        "north": "bathroom",
        "west": "livingRoom",
        "east": "kitchen"
    },
    "garage":{
        "north": "kitchen"
    }
}
location = 'livingRoom'
# print(map['livingRoom']['east'])
def move_player(input):
    # if input is not inside of the map at the players location
        # then tell the user to input a new direction
    # otherwise
        # change the players location to the location stored
        # inside the gamemap at the inputs direction


# 2) Main Game Function
def main():
    global game_over
    # while the game is not over
    while game_over is False:
        # ask the user for inputs
        user_input = input("What would you like to do?")
        # depending on what the user inputs, we do stuff
        # TOOLS: match (multiple if statements), try/except
        match user_input:
            case "help" | "h":
                pass
                # print out to the console the instructions of the game
                # --> function?
            case "north" | "south" | "east" | "west":
                # move the players location to the direction if possible.
                # we will make a function for this
                move_player(user_input)
            case "quit" | "q":
                game_over = True

main()

# --> Handling user input
# INPUTS WE WANT TO HANDLE (Generic):
# investigate
# cardinal directions (north, south, east or west)
# help
# quit / save

# INPUTS WE WANT FOR ROOMS
# --> "would you like to guess the password?" - yes / no
# --> present options as numbers
# 1) Grab the candle
# 2) Lurk around in the dark