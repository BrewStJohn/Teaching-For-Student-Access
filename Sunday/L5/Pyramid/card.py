import pygame as py

class Card(py.sprite.Sprite):
    # 2) Create a class called 'Card' that takes 
    # two parameters (rank and suite)
    def __init__(self, rank, suite):
        # and stores the following properties:
        # - rank
        self.rank = rank
        # - suite
        self.suite = suite
        # - its image
        self.image = py.image.load(f"Pyramid/PNG/Medium/{suite} {rank}.png")
        # - its rect coordinates
        self.rect = self.image.get_rect()

    # CHALLENGE:
    # Give the Card class a method
    # called 'flip'
    # When called, it should flip the card
    # over so we see either the back or
    # the front of it

# TEST:
# Create an instance of the card class and 
# draw it to the screen.
# You should be able to create any type of card
# and test it.