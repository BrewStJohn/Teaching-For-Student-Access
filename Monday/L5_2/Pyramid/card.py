# TODO: Add card class
import pygame

# 2) Create a class called 'card' and store:
class Card(pygame.sprite.Sprite):
    def __init__(self, rank, suite):
        pygame.sprite.Sprite.__init__(self)
        # a) rank
        self.rank = rank
        # b) suite
        self.suite = suite
        # c) Surface
        self.image = pygame.image.load(f"Pyramid\\images\\{suite} {rank}.png")
        # d) Rect
        self.rect = self.image.get_rect()
    

    # CHALLENGE: Create a method called 'flip' that
    # flips the card over so we see its back.