import pygame

class Card(pygame.sprite.Sprite):
    # 2) Create a class called 'Card' that takes 
    # two parameters (rank and suite)
    def __init__(self, rank, suite):
        # and stores the following properties:
        # - rank
        # - suite
        # - its image
        # - its rect coordinates

# TEST:
# Create an instance of the card class and 
# draw it to the screen.
# You should be able to create any type of card
# and test it.