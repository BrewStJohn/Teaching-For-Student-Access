import pygame
# 2) Create a new sprite class called 'Ball'. 
# allow along with the documentation. 
# (GeeksforGeeks - sprites)
# --> The idea here is to create a 
# new visual for the balls!
# CHALLENGE: Create the ball class in its own file

# NOTE: when a function/method inherits 
# methods/properties 
# from another class
# --> parent (base) class, child (derived) class
class Ball(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.path = img_path
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect()


# 3) Create rows and columns of the ball sprites at
# the top. 
# - Create loop that changes the x coordinate 
# of each ball we create --> creating a row
# Create loop that changes the y coordinate 
# of each ball we create --> creating multiple row
# each row alternates between 11 and 10 balls
# IDEA: store each balls x and y coordinates
# IDEA: use a list to store the balls (GROUP!!)
# EXTRA: Add the blue bar at the bottom and change the size of
# the screen

# 4) When you press the left or right buttons
# on your keyboard, print the name of the key you pressed